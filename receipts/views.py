from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Receipt, ReceiptItem, BillSplit
from .forms import ReceiptUploadForm, ReceiptItemForm, BillSplitForm, BillSplitItemForm
import pytesseract
from PIL import Image
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
import uuid

@login_required
def home(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            receipt = Receipt.objects.create(user=request.user)
            receipt.image = request.FILES['image']
            receipt.save()
            # TODO: Add image processing logic here
            return redirect('receipt_detail', receipt_id=receipt.id)
        else:
            messages.error(request, 'Please upload a receipt image.')
            return redirect('home')
    form = ReceiptUploadForm()
    return render(request, 'receipts/home.html', {'form': form})

@login_required
def receipt_history(request):
    receipts = Receipt.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'receipts/receipt_history.html', {'receipts': receipts})

@login_required
def receipt_detail(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
    items = receipt.items.all()
    form = ReceiptItemForm()
    
    if request.method == 'POST':
        form = ReceiptItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.receipt = receipt
            item.save()
            # Recalculate total_amount
            receipt.total_amount = sum(item.price * item.quantity for item in receipt.items.all())
            receipt.save()
            messages.success(request, 'Item added successfully!')
            return redirect('receipt_detail', receipt_id=receipt.id)
    
    # Generate sharing link if it doesn't exist
    if not receipt.sharing_link:
        receipt.sharing_link = uuid.uuid4()
        receipt.save()
    
    return render(request, 'receipts/receipt_detail.html', {
        'receipt': receipt,
        'items': items,
        'form': form
    })

@login_required
def mark_paid(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
    receipt.is_paid = True
    receipt.save()
    messages.success(request, 'Receipt marked as paid!')
    return redirect('receipt_detail', receipt_id=receipt.id)

@login_required
def delete_receipt(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
    receipt.delete()
    messages.success(request, 'Receipt deleted successfully!')
    return redirect('home')

@login_required
def split_bill(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
    items = receipt.items.all()
    splits = receipt.splits.all()
    split_form = BillSplitForm()
    item_form = BillSplitItemForm(receipt=receipt)

    if request.method == 'POST':
        split_form = BillSplitForm(request.POST)
        item_form = BillSplitItemForm(request.POST, receipt=receipt)
        if split_form.is_valid() and item_form.is_valid():
            split = split_form.save(commit=False)
            split.receipt = receipt
            split.save()
            for item in item_form.cleaned_data['items']:
                split.items.add(item)
            split.save()
            messages.success(request, 'Split added successfully!')
            return redirect('split_bill', receipt_id=receipt.id)

    return render(request, 'receipts/split_bill.html', {
        'receipt': receipt,
        'items': items,
        'splits': splits,
        'split_form': split_form,
        'item_form': item_form
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def shared_receipt(request, sharing_link):
    receipt = get_object_or_404(Receipt, sharing_link=sharing_link)
    items = receipt.items.all()
    return render(request, 'receipts/shared_receipt.html', {
        'receipt': receipt,
        'items': items
    })

@login_required
def generate_sharing_link(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
    if not receipt.sharing_link:
        receipt.sharing_link = uuid.uuid4()
        receipt.save()
    return JsonResponse({
        'sharing_link': request.build_absolute_uri(f'/shared/{receipt.sharing_link}/')
    })

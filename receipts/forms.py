from django import forms
from .models import Receipt, ReceiptItem, BillSplit

class ReceiptUploadForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['image']

class ReceiptItemForm(forms.ModelForm):
    class Meta:
        model = ReceiptItem
        fields = ['name', 'price', 'quantity']
        widgets = {
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'min': '1'})
        }

class BillSplitForm(forms.ModelForm):
    class Meta:
        model = BillSplit
        fields = ['person_name', 'amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'})
        }

class BillSplitItemForm(forms.Form):
    items = forms.ModelMultipleChoiceField(
        queryset=ReceiptItem.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        receipt = kwargs.pop('receipt', None)
        super().__init__(*args, **kwargs)
        if receipt:
            self.fields['items'].queryset = receipt.items.all() 
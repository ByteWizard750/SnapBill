from django.db import models
from django.contrib.auth.models import User
import uuid

class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='receipts/', null=True, blank=True)
    merchant_name = models.CharField(max_length=200, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    sharing_link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Receipt {self.id} - {self.merchant_name or 'Unknown'}"

class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class BillSplit(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='splits')
    person_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField(ReceiptItem, blank=True)
    
    def __str__(self):
        return f"{self.person_name} - ${self.amount}"

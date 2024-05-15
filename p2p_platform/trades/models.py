from django.db import models
from users.models import User

class TradeOffer(models.Model):
    TRADE_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trade_type = models.CharField(choices=TRADE_TYPE_CHOICES, max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_details = models.TextField()  # Store payment details for fiat transactions
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    offer = models.ForeignKey(TradeOffer, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name='transactions_as_buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='transactions_as_seller', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
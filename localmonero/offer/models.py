from django.db import models
from django.contrib.auth.models import User

class Offer(models.Model):
    OFFER_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ]

    PAYMENT_METHOD_CHOICES = [
        ('btc', 'Bitcoin (BTC)'),
        ('xmr', 'Monero (XMR)'),
        ('localmonero', 'LocalMonero')
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    offer_type = models.CharField(max_length=4, choices=OFFER_TYPE_CHOICES)
    cryptocurrency = models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=8)
    against = models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES, default='localmonero')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, default='',choices=[('active','Active'),('pending','Pending'),('completed','Completed'),('cancelled','Cancelled')])
    updated = models.DateTimeField(auto_now=True)
    details = models.TextField()
    txid = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.offer_type} {self.amount} {self.cryptocurrency} for {self.price}"



class Transaction(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, default='',choices=[('pending','Pending'),('completed','Completed')])
    updated = models.DateTimeField(auto_now=True)
    coin = models.CharField(max_length=15, choices=[('btc','BTC'),('xmr','XMR')])
    txid = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.offer} {self.buyer} {self.status}"
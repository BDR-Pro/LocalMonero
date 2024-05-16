from django.contrib import admin

# Register your models here.
from .models import User,Review
from trades.models import TradeOffer, Transaction
 
admin.site.register(User)
admin.site.register(TradeOffer)
admin.site.register(Transaction)
admin.site.register(Review)
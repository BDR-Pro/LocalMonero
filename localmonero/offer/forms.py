from django import forms
from .models import Offer

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['offer_type', 'cryptocurrency', 'amount', 'price', 'details', 'against']

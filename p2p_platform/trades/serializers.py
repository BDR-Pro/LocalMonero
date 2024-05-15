from rest_framework import serializers
from .models import TradeOffer, Transaction
from users.serializers import UserSerializer

class TradeOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeOffer
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class Transaction(serializers.ModelSerializer):
    offer = TradeOfferSerializer()
    buyer = UserSerializer()
    seller = UserSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'


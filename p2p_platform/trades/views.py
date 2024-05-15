from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TradeOffer, Transaction
from .serializers import TradeOfferSerializer, TransactionSerializer
from .Monero import create_address, withdraw, get_website_address

class TradeOfferViewSet(viewsets.ModelViewSet):
    queryset = TradeOffer.objects.all()
    serializer_class = TradeOfferSerializer

    @action(detail=True, methods=['post'])
    def initiate_trade(self, request, pk=None):
        offer = self.get_object()
        buyer = request.user
        transaction = Transaction.objects.create(
            offer=offer,
            buyer=buyer,
            seller=offer.user,
            amount=offer.amount,
            status='pending'
        )
        return Response({"transaction_id": transaction.id})

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=True, methods=['post'])
    def complete_trade(self, request, pk=None):
        transaction = self.get_object()
        transaction.status = 'completed'
        transaction.completed_at = timezone.now()
        transaction.save()
        return Response({"status": "Trade completed"})
    
    
    
    

class TradeOfferViewSet(viewsets.ModelViewSet):
    queryset = TradeOffer.objects.all()
    serializer_class = TradeOfferSerializer

    @action(detail=False, methods=['post'])
    def deposit(self, request):
        address = create_address() # type: ignore
        return Response({"address": address})

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        transaction = self.get_object()
        address = request.data.get('address')
        amount = transaction.amount*0.99
        #withdraw the amount to the buyer from the seller
        tx_hash = withdraw(seller_add , address, amount) # type: ignore
        #pay the website fee
        website_fee = transaction.amount*0.01
        website_address = get_website_address() # type: ignore
        withdraw(seller_add ,website_address , website_fee) # type: ignore
        transaction.status = 'completed'
        transaction.completed_at = timezone.now()
        transaction.save()
        return Response({"tx_hash": tx_hash})
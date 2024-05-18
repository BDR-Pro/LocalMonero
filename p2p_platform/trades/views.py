from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.utils import timezone
from .models import Transaction, User, TradeOffer
from users.models import Review
from users.serializers import ReviewSerializer
from .serializers import TransactionSerializer, UserSerializer, TradeOfferSerializer
from .Monero import create_address as create_monero_address, withdraw as withdraw_monero, get_wallet as get_monero_wallet
from .btc import get_new_address as get_btc_new_address, send_to_address as send_btc_to_address
import time

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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
            against_btc=offer.against_btc,
            addy=create_address_for_offer(offer.against_btc),
            status='pending'
        )
        return Response({"transaction_id": transaction.id})

    @action(detail=False, methods=['post'])
    def deposit(self, request):
        address = create_monero_address()
        return Response({"address": address})

def create_address_for_offer(against_btc):
    if against_btc:
        return get_btc_new_address()
    return create_monero_address()

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

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        if request.user.is_anonymous:
            return Response({"error": "You must be logged in to complete a transaction"}, status=status.HTTP_401_UNAUTHORIZED)
        transaction = self.get_object()
        if transaction.buyer != request.user:
            return Response({"error": "You are not the buyer of this transaction"}, status=status.HTTP_403_FORBIDDEN)
        if transaction.status != 'pending':
            return Response({"error": "This transaction is not pending"}, status=status.HTTP_400_BAD_REQUEST)
        if transaction.offer.against_btc:
            return self.exchange_btc_to_monero(transaction)
        address = request.data.get('address')
        amount = transaction.amount
        website_address = get_monero_wallet()
        tx_hash = withdraw_monero(transaction.seller.address, website_address, amount)
        website_fee = amount * 0.99
        withdraw_monero(website_address, address, website_fee)
        transaction.status = 'completed'
        transaction.completed_at = timezone.now()
        transaction.save()
        return Response({"tx_hash": tx_hash})

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        if request.user.is_anonymous:
            return Response({"error": "You must be logged in to cancel a transaction"}, status=status.HTTP_401_UNAUTHORIZED)
        transaction = self.get_object()
        if transaction.buyer != request.user:
            return Response({"error": "You are not the buyer of this transaction"}, status=status.HTTP_403_FORBIDDEN)
        if transaction.status != 'pending':
            return Response({"error": "This transaction is not pending"}, status=status.HTTP_400_BAD_REQUEST)
        transaction.status = 'cancelled'
        transaction.save()
        return Response({"status": "Trade cancelled"})

    def exchange_btc_to_monero(self, transaction):
        """Exchange BTC to Monero"""
        try:
            buyer = transaction.buyer
            seller = transaction.seller
            btc_amount = transaction.amount

            # Step 1: Generate BTC escrow address for the transaction
            btc_escrow_address = get_btc_new_address()

            # Step 2: Wait for BTC payment confirmation (simplified)
            while not self.is_btc_payment_confirmed(btc_escrow_address, btc_amount):
                print("Waiting for BTC payment confirmation...")
                time.sleep(10)

            # Step 3: Generate Monero escrow address for the transaction
            monero_escrow_address = get_monero_wallet()

            # Step 4: Seller sends Monero to Monero escrow address
            while not self.is_monero_payment_confirmed(monero_escrow_address):
                print("Waiting for Monero payment confirmation...")
                time.sleep(10)

            # Step 5: Send BTC to the seller from BTC escrow address
            send_btc_to_address(seller.btc_address, btc_amount)

            # Update the transaction status
            transaction.status = 'completed'
            transaction.save()

            return Response({"status": "Exchange completed"}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"An error occurred: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ExchangeView(APIView):
    def post(self, request, transaction_id):
        """Exchange BTC to Monero"""
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            return TransactionViewSet().exchange_btc_to_monero(transaction)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"An error occurred: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

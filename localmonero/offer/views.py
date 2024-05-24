from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Offer, Transaction
from web.utils.Monero import withdraw as send_monero
from web.utils.btc import send_to_address
from .forms import OfferForm
from django.contrib.auth.models import User

def get_addresses(crypto, offer):
    if crypto == 'BTC':
        website_address = User.objects.get(username='bader').profile.btc_address
        user_address = offer.seller.profile.btc_address
    elif crypto == 'XMR':
        website_address = User.objects.get(username='bader').profile.xmr_address
        user_address = offer.seller.profile.xmr_address
    return website_address, user_address


def perform_transaction(offer):
    offer.cryptocurrency = offer.cryptocurrency.upper()
    offer.cryptocurrency = offer.cryptocurrency if offer.offer_type == 'SELL' else offer.against
    website_address, user_address = get_addresses(offer.cryptocurrency,offer)
    if offer.cryptocurrency == 'BTC':
        txid = send_to_address(user_address, website_address, offer.amount)
    elif offer.cryptocurrency == 'XMR':
        txid = send_monero(user_address, website_address, offer.amount)
    if txid:
        offer.status = 'ACTIVE'
        offer.txid = txid
        offer.save()

def threading_perform_transaction(offer):
    from threading import Thread
    t = Thread(target=perform_transaction, args=(offer,))
    t.start()

@login_required
def new_offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.seller = request.user
            offer.status = 'PENDING'
            offer.save()
            threading_perform_transaction(offer)
            return redirect('offer:offer_detail', offer_id=offer.id)
            
    else:
        form = OfferForm()
    return render(request, 'offer/new_offer.html', {'form': form})

@login_required
def offer_list(request):
    offer = Offer.objects.all()
    return render(request, 'offer/offer_list.html', {'offers': offer,'count':offer.count()})

@login_required
def offer_detail(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    return render(request, 'offer/offer_detail.html', {'offer': offer})

@login_required
def offer_edit(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    if offer.seller != request.user:
        return redirect('offer:offer_list')
    if request.method == 'POST':
        form = OfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('offer:offer_detail', offer_id=offer.id)
    else:
        form = OfferForm(instance=offer)
    return render(request, 'offer/offer_edit.html', {'form': form})

@login_required
def offer_delete(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    if offer.seller != request.user:
        return redirect('offer:offer_list')
    offer.delete()
    return redirect('offer:offer_list')

@login_required
def offer_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if not query:
            return render(request, 'offer/offer_search.html')
        results = Offer.objects.filter(details__icontains=query)
        return render(request, 'offer/offer_search.html', {'results': results, 'query': query})
    return render(request, 'offer/offer_search.html')

def complete_transaction(transaction):
    transaction.status = 'COMPLETED'
    transaction.save()
    offer = transaction.offer
    offer.status = 'COMPLETED' if offer.amount == transaction.amount else 'ACTIVE'
    offer.amount -= transaction.amount
    offer.save()
    close_deal(transaction)

#? ANything wrong with this function?

def close_deal(transaction):
    #send money from website to the one who bought the offer
    
    website_address, seller_address = get_addresses(transaction.coin, transaction.offer)
    #TODO: Implement the send_to_address function
def threading_complete_transaction(transaction):
    from threading import Thread
    t = Thread(target=complete_transaction, args=(transaction,))
    t.start()

@login_required
def init_transaction(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    if offer.seller == request.user:
        return redirect('offer:offer_detail', offer_id=offer.id)

    if request.method == 'GET':
        return render(request, 'offer/init_transaction.html', {'offer': offer})

    if request.method == 'POST':
        amount = request.POST.get('amount')
        coin = request.POST.get('coin')

        if amount is None or coin not in ['BTC', 'XMR']:
            return render(request, 'offer/init_transaction.html', {'offer': offer, 'error': 'Invalid amount or coin'})
        if float(amount) > offer.amount:
            return render(request, 'offer/init_transaction.html', {'offer': offer, 'error': 'Amount is greater than the offer'})
        if offer.status != 'ACTIVE':
            return render(request, 'offer/init_transaction.html', {'offer': offer, 'error': 'Offer is not active'})
        
        Transaction.objects.create(offer=offer, buyer=request.user,coin=coin, status='PENDING', txid='')
        
        # * Perform transaction based on the coin and amount and the seller address and website address
        # TODO: Implement this function
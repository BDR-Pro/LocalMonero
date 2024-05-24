from django.shortcuts import render

# Create your views here.
#fund_localmonero_account withdraw_localmonero withdraw_btc withdraw_xmr 

def fund_localmonero_account(request):
    return render(request, 'funds/fund_localmonero_account.html')


def withdraw_localmonero(request):
    #withdraw in usdt
    return render(request, 'funds/withdraw_localmonero.html')

def withdraw_btc(request):
    return render(request, 'funds/withdraw_btc.html')

def withdraw_xmr(request):
    return render(request, 'funds/withdraw_xmr.html')


from web.views import health_check, isMoneroUp, isBitcoinUp, getBalance,createWalletBTC,sendBTC,checkBalanceByAddressBTC

from django.urls import path

app_name = 'web'

urlpatterns = [
    
    path('health_check/', health_check, name='health_check'),
    path('isMoneroUp/', isMoneroUp, name='isMoneroUp'),
    path('isBitcoinUp/', isBitcoinUp, name='isBitcoinUp'),
    path('getBalance/', getBalance, name='getBalance'),
    path('createWalletBTC/', createWalletBTC, name='createWalletBTC'),
    path('sendBTC/', sendBTC, name='sendBTC'),
    path('checkBalanceByAddressBTC/', checkBalanceByAddressBTC, name='checkBalanceByAddressBTC'),
    
]
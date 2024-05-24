from django.urls import path
from  .views import fund_localmonero_account ,withdraw_localmonero ,withdraw_btc ,withdraw_xmr 

app_name = 'funds'

urlpatterns = [
 
    path('', fund_localmonero_account, name='fund_localmonero_account'),
    path('withdraw', withdraw_localmonero, name='withdraw_localmonero'),
    path('withdraw_btc/', withdraw_btc, name='withdraw_btc'),
    path('withdraw_xmr/', withdraw_xmr, name='withdraw_xmr'),
 
]
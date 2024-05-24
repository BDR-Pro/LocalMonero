from user.views import login, register, profile, logout,calculate_xmr_balance, calculate_btc_balance

from django.urls import path

app_name = 'user'

urlpatterns = [
    
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('calculate_xmr_balance/', calculate_xmr_balance, name='calculate_xmr_balance'),
    path('calculate_btc_balance/', calculate_btc_balance, name='calculate_btc_balance'),
]
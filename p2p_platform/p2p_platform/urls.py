from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet,RegisterView    
from trades.views import TradeOfferViewSet, TransactionViewSet, ExchangeView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trade_offers', TradeOfferViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('health/', include('health_check.urls')),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/exchange/<int:transaction_id>/', ExchangeView.as_view(), name='exchange_btc_to_monero'),
]
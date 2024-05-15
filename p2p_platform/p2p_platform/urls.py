from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from trades.views import TradeOfferViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trade_offers', TradeOfferViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
from django.urls import path
from .views import health_check, isMoneroUp
urlpatterns = [
    path('', health_check),
    path('monero/', isMoneroUp),
]
from django.urls import path
from .views import new_offer, offer_list, offer_detail, offer_edit, offer_delete, offer_search,init_transaction

app_name = 'offer'
urlpatterns = [
    path('new/', new_offer, name='new_offer'),
    path('', offer_list, name='offer_list'),
    path('<int:offer_id>/', offer_detail, name='offer_detail'),
    path('<int:offer_id>/edit/', offer_edit, name='offer_edit'),
    path('<int:offer_id>/delete/', offer_delete, name='offer_delete'),
    path('search/', offer_search, name='offer_search'),
    path('buy/<int:offer_id>/', init_transaction, name='init_transction')
]

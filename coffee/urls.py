# coffee/urls.py

from django.urls import path
from .views import add_to_cart, home, initiate_payment

urlpatterns = [
    path('',home , name='home'),
    # path('add/<int:product_id>/', add_to_cart, name='add-item'),
    path('initiate_payment/', initiate_payment, name='initiate_payment'),

    # Other URL patterns
]

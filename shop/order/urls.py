from django.urls import path
from order.views import cart_add, item_clear, item_decrement, item_increment, cart_clear, cart_detail, address_confirmation

app_name = 'order'
urlpatterns = [
    path('cart/address_confirmation/', address_confirmation, name='address_confirmation'),

    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
]

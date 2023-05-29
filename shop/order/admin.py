from django.contrib import admin
from order.models import Order, OrderItem


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'delivery_address']
    list_filter = ['status']

    list_per_page = 50
    search_fields = ['user']


@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'quantity']
    raw_id_fields = ('order', )
    list_per_page = 50
    search_fields = ['order']

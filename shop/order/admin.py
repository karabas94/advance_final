from django.contrib import admin
from order.models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['user', 'status', 'delivery_address', 'braintree_id']
    list_filter = ['status']
    list_per_page = 50
    search_fields = ['user']

import requests
from celery import shared_task
from order.models import Order, OrderItem
from django.contrib.auth import get_user_model

user = get_user_model()


@shared_task
def send_new_orders_to_store():
    new_orders = Order.objects.filter(status=Order.OrderStatus.ORDER)

    for order in new_orders:
        url = 'http://store:8000/orders/'
        api_key = '5O8boh3b.sBX6dm403uefUTvnBWBhkcN3AaQlE5Oy'
        headers = {
            'Authorization': f'Api-Key {api_key}'
        }
        order_items = OrderItem.objects.filter(order=order)

        order_items_data = list(map(lambda order_item: {
            "book_store": order_item.book.id_in_store,
            "quantity": order_item.quantity}, order_items))

        data = {
            "user_email": order.user.email,
            "status": 1,
            "delivery_address": order.delivery_address,
            "order_id_in_shop": order.id,
            "order_items": order_items_data,
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            print('Order sent to store successfully')

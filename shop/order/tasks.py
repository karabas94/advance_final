import requests
from order.models import Order, OrderItem
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_order_success_emails(user_email):
    subject = 'Order sent'
    message = 'Thank you for your order!'
    from_email = 'noreply@bookshop.com'
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


@shared_task
def send_order_confirmation_email(user_email):
    subject = 'Order Confirmation'
    message = 'Thank you for your order!'
    from_email = 'noreply@bookshop.com'
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


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


@shared_task
def update_order_status_to_shop():
    url_orders = 'http://store:8000/orders/'
    response = requests.get(url_orders).json()

    for order in response.get('results', []):
        order_id_in_shop = order.get('order_id_in_shop')
        status = order.get('status')

        try:
            order = Order.objects.get(id=order_id_in_shop)
            if status == 3:
                order.status = 3
                order.save()
            elif status == 4:
                order.status = 4
                order.save()
        except Order.DoesNotExist:
            pass

    print('Order status updated in shop')

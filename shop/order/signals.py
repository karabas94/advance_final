from order.models import Order
from order.tasks import send_order_success_emails


def send_order_email(sender, instance, created, **kwargs):
    if instance.status == Order.OrderStatus.SUCCESS:
        send_order_success_emails.delay(instance.user.email)

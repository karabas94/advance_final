from django.apps import AppConfig
from django.db.models.signals import post_save


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'

    def ready(self):
        from order.models import Order
        from order.signals import send_order_email
        post_save.connect(send_order_email, sender=Order)

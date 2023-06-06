from django.apps import AppConfig
from django.db.models.signals import post_save


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        from store.models import Order
        from store.signals import delete_related_book_items
        post_save.connect(delete_related_book_items, sender=Order)

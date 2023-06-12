from django.apps import AppConfig
from django.db.models.signals import post_save


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'

    def ready(self):
        from book.signals import send_notification_review_mail
        from book.models import Review
        post_save.connect(send_notification_review_mail, sender=Review)

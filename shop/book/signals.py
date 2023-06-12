from django.core.mail import send_mail


def send_notification_review_mail(sender, instance, **kwargs):
    if not instance.is_reviewed:
        send_mail(
            'New Review',
            f"A new review has been added to '{instance.book.name}' by '{instance.author.username}':\n\n{instance.message}",
            'noreply@admin.com',
            ['admin@admin.com'],
            fail_silently=False,
        )

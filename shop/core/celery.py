import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'book_to_shop': {
        'task': 'book.tasks.send_new_book_to_shop',
        'schedule': crontab(minute="*")
    },

    'order_to_store': {
        'task': 'order.tasks.send_new_orders_to_store',
        'schedule': crontab(minute="*")
    }
}

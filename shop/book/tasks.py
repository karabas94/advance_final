import requests  # noqa
from celery import shared_task
from book.models import Book


@shared_task
def book_synch():
    url_books = 'http://store:8000/books/'
    response = requests.get(url_books).json()
    while True:
        for counter, book in enumerate(response['results']):
            data, created = Book.objects.get_or_create(
                id_in_store=book['id'],
                defaults={
                    'title': book['title'],
                    'price': book['price'],
                    'quantity': 1,
                }

            )
            if not created:
                data.title = book['title']
                data.price = book['price']
                data.quantity = 1
                data.save()

        if response['next']:
            response = requests.get(response['next']).json()
        else:
            break

    print('Success')


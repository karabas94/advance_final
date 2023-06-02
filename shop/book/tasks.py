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
                    'name': book['name'],
                    'price': book['price'],
                    'quantity': book['quantity'],
                    'image': 'products/default_book_image.jpeg'
                }

            )
            if not created:
                data.name = book['name']
                data.price = book['price']
                data.quantity = book['quantity']
                data.image = 'products/default_book_image.jpeg'
                data.save()

        if response['next']:
            response = requests.get(response['next']).json()
        else:
            break

    print('Success')

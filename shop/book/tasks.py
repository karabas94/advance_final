from urllib.parse import urlparse

import requests
from celery import shared_task
from book.models import Author, Genre, Book


@shared_task
def send_new_book_to_shop_or_update():
    url_books = 'http://store:8001/books/'
    response = requests.get(url_books).json()

    store_book_ids = [book['id'] for book in response['results']]
    for book in Book.objects.all():
        if book.id_in_store not in store_book_ids:
            book.delete()

    while True:
        for book_data in response['results']:

            author_data = book_data['author'][0]
            author, _ = Author.objects.update_or_create(
                id=author_data['id'],
                defaults={
                    'first_name': author_data['first_name'],
                    'last_name': author_data['last_name'],
                    'bio': author_data['bio']
                }
            )

            genre_data_list = book_data['genre']
            genres = []
            for genre_data in genre_data_list:
                genre, _ = Genre.objects.update_or_create(
                    id=genre_data['id'],
                    defaults={'name': genre_data['name']}
                )
                genres.append(genre)

            book_items = book_data['book_items']
            book_quantity = len(book_items)

            image_url = book_data['image']
            parsed_url = urlparse(image_url)
            image_path = parsed_url.path
            segments = image_path.split('/')
            image_filename = '/'.join(segments[-2:])

            book, created = Book.objects.update_or_create(
                id_in_store=book_data['id'],
                defaults={
                    'name': book_data['name'],
                    'price': book_data['price'],
                    'quantity': book_quantity,
                    'image': image_filename,
                    'author': author,
                    'publication_year': book_data['publication_year'],
                    'description': book_data['description'],
                    'pages': book_data['pages']
                }
            )
            book.genre.set(genres)

        if response['next']:
            response = requests.get(response['next']).json()
            store_book_ids += [book['id'] for book in response['results']]
        else:
            break

    print('Books updated from store to shop')

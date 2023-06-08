import requests
from celery import shared_task
from book.models import Book


# @shared_task
# def send_new_book_to_shop_or_update():
#     url_books = 'http://store:8001/books/'
#     response = requests.get(url_books).json()
#
#     store_book_ids = [book['id'] for book in response['results']]
#     for book in Book.objects.all():
#         if book.id_in_store not in store_book_ids:
#             book.delete()
#
#     while True:
#         for counter, book in enumerate(response['results']):
#             book_items = book['book_items']
#             book_quantity = len(book_items)
#
#             data, created = Book.objects.get_or_create(
#                 id_in_store=book['id'],
#                 defaults={
#                     'name': book['name'],
#                     'price': book['price'],
#                     'quantity': book_quantity,
#                     'image': 'products/default_book_image.jpeg'
#                 }
#             )
#
#             if not created:
#                 data.name = book['name']
#                 data.price = book['price']
#                 data.quantity = book_quantity
#                 data.image = 'products/default_book_image.jpeg'
#                 data.save()
#
#         if response['next']:
#             response = requests.get(response['next']).json()
#             store_book_ids += [book['id'] for book in response['results']]
#         else:
#             break
#
#     print('Book updated from store to shop')

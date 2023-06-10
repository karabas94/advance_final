from django.urls import path
from book.views import AuthorListView, AuthorDetailView, BookListView, BookDetailView, add_review

app_name = 'book'
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('<int:pk>/review/', add_review, name='add_review'),
]

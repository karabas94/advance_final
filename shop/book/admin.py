from django.contrib import admin
from book.models import Book, Author, Genre


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_per_page = 50
    search_fields = ['first_name']


@admin.register(Genre)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 50


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'author', 'publication_year', 'pages']
    list_filter = ['price']
    list_per_page = 50
    search_fields = ['name']

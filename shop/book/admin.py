from django.contrib import admin
from book.models import Book


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity']
    list_filter = ['price']
    list_per_page = 50
    search_fields = ['title']
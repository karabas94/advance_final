from django.contrib import admin
from store.models import Book


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['price']
    list_per_page = 50
    search_fields = ['name']

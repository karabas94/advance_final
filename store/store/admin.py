from django.contrib import admin
from store.models import Author, Genre, Book, BookItem, Order, OrderItem


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


class BookItemInline(admin.StackedInline):
    model = BookItem
    extra = 1


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    inlines = [BookItemInline]
    list_display = ['name', 'price', 'author', 'publication_year', 'pages']
    list_filter = ['price']
    list_per_page = 50
    search_fields = ['name']


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['status', 'delivery_address', 'user_email']
    list_filter = ['status']
    list_per_page = 50
    search_fields = ['user']

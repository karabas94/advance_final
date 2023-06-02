from rest_framework import serializers
from store.models import Book, BookItem, Order, OrderItem


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'price', 'quantity']


class BookItemSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = BookItem
        fields = ['url', 'id', 'book', 'place']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'id', 'user_email', 'status', 'delivery_address', 'order_id_in_shop']


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.ReadOnlyField(source='order.status')
    book_store = serializers.ReadOnlyField(source='book.title')
    book_item = BookItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['url', 'id', 'order', 'book_store', 'quantity', 'book_item']

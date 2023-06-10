from rest_framework import serializers
from store.models import Author, Genre, Book, BookItem, Order, OrderItem


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'bio']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ['id', 'place']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SerializerMethodField()
    book_items = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()

    def get_book_items(self, obj):
        book_items = BookItem.objects.filter(book=obj)
        serializer = BookItemSerializer(book_items, many=True)
        return serializer.data

    def get_genre(self, obj):
        genre = Genre.objects.filter(book=obj)
        serializers = GenreSerializer(genre, many=True)
        return serializers.data

    def get_author(self, obj):
        author = Author.objects.filter(book=obj)
        serializers = AuthorSerializer(author, many=True)
        return serializers.data

    class Meta:
        model = Book
        fields = ['url', 'id', 'name', 'price', 'author', 'genre', 'publication_year', 'description',
                  'pages', 'image', 'book_items']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['book_store', 'quantity']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Order
        fields = ['url', 'id', 'user_email', 'status', 'delivery_address', 'order_id_in_shop', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for items_data in order_items_data:
            OrderItem.objects.create(order=order, **items_data)
        return order

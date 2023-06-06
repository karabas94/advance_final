from store.models import Book, BookItem, Order, OrderItem
from store.serializer import BookSerializer, BookItemSerializer, OrderSerializer, OrderItemSerializer
from store.permissions import IsStaffOrReadOnly
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_api_key.permissions import HasAPIKey


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [HasAPIKey | permissions.IsAuthenticatedOrReadOnly, HasAPIKey | IsStaffOrReadOnly]


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [HasAPIKey | permissions.IsAuthenticatedOrReadOnly, HasAPIKey | IsStaffOrReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [HasAPIKey | permissions.IsAuthenticatedOrReadOnly, HasAPIKey | IsStaffOrReadOnly]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [HasAPIKey | permissions.IsAuthenticatedOrReadOnly, HasAPIKey | IsStaffOrReadOnly]

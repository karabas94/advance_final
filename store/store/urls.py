from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename="book")
router.register(r'book_items', views.BookItemViewSet, basename="book_item")
router.register(r'orders', views.OrderViewSet, basename="order")
router.register(r'order_items', views.OrderItemViewSet, basename="order_item")

urlpatterns = [
    path('', include(router.urls)),
]

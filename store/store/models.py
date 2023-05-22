from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)


class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        PROCEED = 1, _('Proceed')
        SUCCESS = 2, _('Success')
        FAIL = 3, _("Fail")

    user_email = models.EmailField()
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices)
    delivery_address = models.CharField(max_length=255)
    order_id_in_shop = models.IntegerField


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_store = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField
    book_item = models.ManyToManyField(BookItem)

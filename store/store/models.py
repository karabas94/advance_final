from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.book.name} - Place {self.place}'


class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        NEW = 1, _('New')
        PROCEED = 2, _('Proceed')
        # SUCCESS signal to delete book items
        SUCCESS = 3, _('Success')
        FAIL = 4, _("Fail")

    user_email = models.EmailField()
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices)
    delivery_address = models.CharField(max_length=255)
    order_id_in_shop = models.IntegerField(unique=True)

    def __str__(self):
        return self.delivery_address


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_store = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    book_item = models.ManyToManyField(BookItem)

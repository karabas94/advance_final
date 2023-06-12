from django.db import models
from django.conf import settings
from django.db.models import Sum, F
from django.utils.translation import gettext_lazy as _
from book.models import Book


class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        ORDER = 2, _('Order')
        SUCCESS = 3, _('Success')
        FAIL = 4, _("Fail")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices)
    delivery_address = models.CharField(max_length=255)
    braintree_id = models.CharField(max_length=150, blank=True)

    def get_total_cost(self):
        total_cost = self.orderitem_set.aggregate(
            total=Sum(F('quantity') * F('book__price'))
        )['total']
        return total_cost


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)

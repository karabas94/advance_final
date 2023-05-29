from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(null=False)
    id_in_shop = models.IntegerField(unique=True)

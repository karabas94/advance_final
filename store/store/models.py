from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre, blank=True, verbose_name="genre")
    publication_year = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    pages = models.IntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True,)

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

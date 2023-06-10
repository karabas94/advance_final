from django.db import models
from django.conf import settings

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
    quantity = models.IntegerField(null=False)
    id_in_store = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    pages = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.author.username

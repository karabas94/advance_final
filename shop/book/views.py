from django.shortcuts import render
from django.views import generic, View
from book.models import Author, Genre, Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 9


class AuthorDetailView(generic.DetailView):
    model = Author


class BookListView(generic.ListView):
    model = Book
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        genre_id = self.request.GET.get('genre_id')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if genre_id:
            queryset = queryset.filter(genre__id=genre_id)

        return queryset


class BookDetailView(generic.DetailView):
    model = Book

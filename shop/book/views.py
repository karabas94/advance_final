from django.views import generic
from book.models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 29

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class BookDetailView(generic.DetailView):
    model = Book
    
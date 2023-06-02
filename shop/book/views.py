from django.views import generic
from book.models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 29

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BookDetailView(generic.DetailView):
    model = Book

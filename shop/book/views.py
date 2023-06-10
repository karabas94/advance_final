from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.views import generic
from book.models import Author, Book, Review
from book.form import ReviewForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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
        queryset = queryset.select_related('author').annotate(
            review_count=Count('reviews', filter=Q(reviews__is_reviewed=True))).all()
        name = self.request.GET.get('name')
        genre_id = self.request.GET.get('genre_id')

        if name:
            queryset = queryset.filter(name__icontains=name)

        if genre_id:
            queryset = queryset.filter(genre__id=genre_id)

        return queryset


class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.filter(is_reviewed=True)
        paginator = Paginator(reviews, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['reviews'] = page_obj
        return context


# signal(send mail to admin)
@login_required
def add_review(request, pk):
    book = Book.objects.get(pk=pk)
    reviews = book.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.author = request.user
            review.save()
            return redirect('book:book_detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'blog/post_detail.html', {'book': book, 'reviews': reviews, 'form': form})

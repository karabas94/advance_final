from book.models import Genre


def genres(request):
    return {'genres': Genre.objects.all()}
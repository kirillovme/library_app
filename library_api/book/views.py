from book.models import Book
from book.serializers import BookSerializer
from rest_framework import filters, viewsets


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for handling the CRUD operations of the Book model."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

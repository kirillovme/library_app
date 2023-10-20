from author.models import Author
from author.serializers import AuthorSerializer
from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for handling the CRUD operations of the Author model."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

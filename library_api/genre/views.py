from genre.models import Genre
from genre.serializers import GenreSerializer
from rest_framework import viewsets


class GenreViewSet(viewsets.ModelViewSet):
    """ViewSet for handling the CRUD operations of the Genre model."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

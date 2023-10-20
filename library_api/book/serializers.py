from author.serializers import AuthorSerializer
from book.models import Book
from genre.serializers import GenreSerializer
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model."""

    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value: str) -> str:
        """Validate the title of the book."""
        words = value.split()
        if not all(word.isalpha() for word in words):
            raise serializers.ValidationError('Title should only contain alphabetic characters.')
        return value

    def to_representation(self, instance: Book):
        """Modify the representation of the serialized data."""
        response = super().to_representation(instance)
        response['authors'] = AuthorSerializer(instance.authors, many=True).data
        response['genres'] = GenreSerializer(instance.genres, many=True).data
        return response

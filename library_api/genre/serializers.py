from genre.models import Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for the Genre model."""

    class Meta:
        model = Genre
        fields = '__all__'

    def validate_name(self, value: str) -> str:
        """Validate the name of the genre."""
        words = value.split()
        if not all(word.isalpha() for word in words):
            raise serializers.ValidationError('Genre name should only contain alphabetic characters.')
        return value

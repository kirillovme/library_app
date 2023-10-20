from author.models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model."""

    class Meta:
        model = Author
        fields = '__all__'

    def validate_name(self, value: str) -> str:
        """Validate the name of the author."""
        words = value.split()
        if not all(word.isalpha() for word in words):
            raise serializers.ValidationError('Name should only contain alphabetic characters.')
        return value

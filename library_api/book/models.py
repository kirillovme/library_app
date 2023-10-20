import uuid

from django.db import models


class Book(models.Model):
    """Book model representing a book with details like title, authors, and genres."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, unique=True)
    authors = models.ManyToManyField('author.Author')
    genres = models.ManyToManyField('genre.Genre')

    class Meta:
        ordering = ['title']

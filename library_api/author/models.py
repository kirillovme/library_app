import uuid

from django.db import models


class Author(models.Model):
    """Author model representing an author of books."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

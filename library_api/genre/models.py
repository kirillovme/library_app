import uuid
from django.db import models


class Genre(models.Model):
    """Genre model representing a genre of books."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

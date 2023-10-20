# Generated by Django 4.2.6 on 2023-10-20 12:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('authors', models.ManyToManyField(to='author.author')),
                ('genres', models.ManyToManyField(to='genre.genre')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
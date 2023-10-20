import pytest
from author.models import Author
from book.models import Book
from genre.models import Genre
from rest_framework import status
from rest_framework.test import APIClient

BOOK_URL = '/api/books/'


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def author():
    return Author.objects.create(name='Author Name')


@pytest.fixture
def genre():
    return Genre.objects.create(name='Genre Name')


@pytest.fixture
def book_data(author, genre):
    return {
        'title': 'Book Title',
        'authors': [author.id],
        'genres': [genre.id]
    }


@pytest.mark.django_db
def test_create_book(api_client, book_data):
    response = api_client.post(BOOK_URL, book_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.count() == 1


@pytest.mark.django_db
def test_get_books(api_client, book_data):
    api_client.post(BOOK_URL, book_data, format='json')
    response = api_client.get(BOOK_URL)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1


@pytest.mark.django_db
def test_update_book(api_client, book_data):
    response = api_client.post(BOOK_URL, book_data, format='json')
    book_id = response.data['id']
    updated_data = {'title': 'Updated Book Title'}
    response = api_client.patch(f'{BOOK_URL}{book_id}/', updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_delete_book(api_client, book_data):
    response = api_client.post(BOOK_URL, book_data, format='json')
    book_id = response.data['id']
    response = api_client.delete(f'{BOOK_URL}{book_id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Book.objects.count() == 0

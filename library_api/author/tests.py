import pytest
from author.models import Author
from rest_framework import status
from rest_framework.test import APIClient

AUTHOR_URL = '/api/authors/'


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def author_data():
    return {'name': 'Jane Doe'}


@pytest.fixture
def save_author():
    def _save_author(name='Jane Doe'):
        return Author.objects.create(name=name)

    return _save_author


@pytest.mark.django_db
def test_create_author(api_client, author_data):
    response = api_client.post(AUTHOR_URL, author_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Author.objects.count() == 1


@pytest.mark.django_db
def test_get_authors(api_client, save_author):
    save_author()
    response = api_client.get(AUTHOR_URL)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1


@pytest.mark.django_db
def test_update_author(api_client, save_author):
    author = save_author()
    updated_data = {'name': 'Jane Smith'}
    response = api_client.put(f'{AUTHOR_URL}{author.id}/', updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    author.refresh_from_db()
    assert author.name == 'Jane Smith'


@pytest.mark.django_db
def test_delete_author(api_client, save_author):
    author = save_author()
    response = api_client.delete(f'{AUTHOR_URL}{author.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Author.objects.count() == 0

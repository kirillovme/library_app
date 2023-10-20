import pytest
from genre.models import Genre
from rest_framework import status
from rest_framework.test import APIClient

GENRE_URL = '/api/genres/'


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def genre_data():
    return {'name': 'Fiction'}


@pytest.fixture
def save_genre():
    def _save_genre(name='Fiction'):
        return Genre.objects.create(name=name)
    return _save_genre


@pytest.mark.django_db
def test_create_genre(api_client, genre_data):
    response = api_client.post(GENRE_URL, genre_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Genre.objects.count() == 1


@pytest.mark.django_db
def test_get_genres(api_client, save_genre):
    save_genre()
    response = api_client.get(GENRE_URL)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1


@pytest.mark.django_db
def test_update_genre(api_client, save_genre):
    genre = save_genre()
    updated_data = {'name': 'Non Fiction'}
    response = api_client.put(f'{GENRE_URL}{genre.id}/', updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    genre.refresh_from_db()
    assert genre.name == 'Non Fiction'


@pytest.mark.django_db
def test_delete_genre(api_client, save_genre):
    genre = save_genre()
    response = api_client.delete(f'{GENRE_URL}{genre.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Genre.objects.count() == 0

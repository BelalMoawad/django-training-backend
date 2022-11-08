import pytest
import json
from artists.models import Artist
from albums.models import Album
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()


@pytest.mark.django_db
class TestCreateAlbums:
    def test_get_all_albums(self):
        artist1 = Artist.objects.create(
            stage_name="artist1",
            social_link="https://www.facebook.com/1/"
        )
        artist2 = Artist.objects.create(
            stage_name="artist2",
            social_link="https://www.facebook.com/2/"
        )
        Album.objects.create(
            album_name="album1",
            releasing_date="2020-01-01",
            album_cost=100,
            artist=artist1,
            approved=True
        )
        Album.objects.create(
            album_name="album2",
            releasing_date="2020-01-02",
            album_cost=200,
            artist=artist2,
            approved=False
        )
        Album.objects.create(
            album_name="album3",
            releasing_date="2020-01-03",
            album_cost=300,
            artist=artist2,
            approved=True
        )
        url = reverse('albums')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
    
    def test_post_album(self) :
        artist = Artist.objects.create(
            stage_name="artist",
            social_link="https://www.facebook.com/"
        )
        data = {
            "album_name" : "album",
            "releasing_date" : "2020-01-01",
            "album_cost" : 100,
            "artist" : artist.pk,
            "approved" : True
        }
        url = reverse('albums')
        response = client.post(url, data = data, format = 'json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_album_to_artist_not_exist(self) :
        data = {
            "album_name" : "album",
            "releasing_date" : "2020-01-01",
            "album_cost" : 100,
            "artist" : 4,
            "approved" : True
        }
        url = reverse('albums')
        response = client.post(url, data = data, format = 'json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_album_missing_artist(self) :
        data = {
            "album_name" : "album",
            "releasing_date" : "2020-01-01",
            "album_cost" : 100,
            "approved" : True
        }
        url = reverse('albums')
        response = client.post(url, data = data, format = 'json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST    

    def test_post_missing_all_data(self) :
        url = reverse('albums')
        response = client.post(url, data = {}, format = 'json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

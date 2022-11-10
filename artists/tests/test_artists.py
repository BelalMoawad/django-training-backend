import pytest
from artists.models import Artist
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()

@pytest.mark.django_db
class TestCreateArtists :
    def test_posting_artist(self) :
        data = {
            "stage_name" : "drake",
            "social_link" : "https://www.instagram.com/drake/"
        }
        url = reverse('artists')
        response = client.post(url, data = data, format = 'json')  
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_posting_artist_with_missing_data(self) :
        data = {
            "stage_name" : "",
            "social_link" : "https://www.instagram.com/drake/"
        }
        url = reverse('artists')
        response = client.post(url, data = data, format = 'json')  
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_posting_artist_with_invalid_social_link(self) :
        data = {
            "stage_name" : "drake",
            "social_link" : "testing"
        }
        url = reverse('artists')
        response = client.post(url, data = data, format = 'json')  
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_all_artists(self) :
        url = reverse('artists')
        response = client.get(url)  
        assert response.status_code == status.HTTP_200_OK

    def test_get_specific_artist(self) :
        art = Artist.objects.create(
            stage_name = "drake",
            social_link = "https://www.instagram.com/drake/"
        )
        url = reverse('artist', kwargs={'pk' : art.pk})
        response = client.get(url)  
        assert response.status_code == status.HTTP_200_OK
import pytest
import json
from artists.models import Artist
from albums.models import Album
from users.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from albums.serializers import AlbumSerializer


def Convert_Album_To_Json(album) :
    return {
        "id" : album.id,
        "album_name" : album.album_name,
        "creation_date" : album.creation_date,
        "releasing_date" : album.releasing_date,
        "album_cost" : float(album.album_cost),
        "approved" : album.approved,
        "artist" : album.artist.id
    }


client = APIClient()
@pytest.mark.django_db
class TestSerializers :
    def test_serializing(self) :
        user = User.objects.create(
            username = "abcd",
            password = "12345" 
        )
        artist = Artist.objects.create(
            stage_name = "stage",
            social_link = "https://www.facebook.com/",
            user = user
        )
        album = Album.objects.create(
            album_name="album",
            releasing_date="2020-01-01",
            album_cost=100,
            artist=artist,
            approved=True
        )
        serializer = AlbumSerializer(album)
        manual_serializer = Convert_Album_To_Json(album)
        assert manual_serializer["id"] == serializer.data["id"]
        assert manual_serializer["album_name"] == serializer.data["album_name"]
        assert manual_serializer["releasing_date"] == serializer.data["releasing_date"]
        assert manual_serializer["album_cost"] == serializer.data["album_cost"]
        assert manual_serializer["approved"] == serializer.data["approved"]
        assert manual_serializer["artist"] == serializer.data["artist"]
from rest_framework import serializers
from .models import Album, Song

 
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'album_name', 'creation_date', 'releasing_date',
                  'album_cost', 'artist', 'approved']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'song_name', 'img', 'img_thumbnail', 'album']
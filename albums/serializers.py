from rest_framework import serializers
from .models import Album

 
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'album_name', 'creation_date', 'releasing_date',
                  'album_cost', 'artist', 'approved']


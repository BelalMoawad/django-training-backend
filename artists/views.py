from albums.models import Album
from albums.serializers import AlbumSerializer
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class ArtistsView(APIView) :
    def get(self, request, *args, **kwargs) :
        allArtists = Artist.objects.all()
        serializer = ArtistSerializer(allArtists, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs) :
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistView(APIView) :
    def get(self, request, *args, **kwargs) :
        singleArtist = Artist.objects.all().get(stage_name = kwargs["id"])
        serializer1 = ArtistSerializer(singleArtist)
        singleArtistAlbums = Album.objects.all().filter(artist=singleArtist)
        serializer = AlbumSerializer(singleArtistAlbums, many=True)
        return Response([serializer1.data, serializer.data])     



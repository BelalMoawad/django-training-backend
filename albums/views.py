from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class AlbumView(APIView) :
    def get(self, request, *args, **kwargs) :
        allAlbums = Album.objects.all()
        serializer = AlbumSerializer(allAlbums, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs) :
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                   

class SongView(APIView) :
    def get(self, request, *args, **kwargs) :
        allSongs = Song.objects.all()
        serializer = SongSerializer(allSongs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs) :
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    





    


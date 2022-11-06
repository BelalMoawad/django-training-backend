from .models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class AlbumView(APIView) :
    permission_classes = [permissions.AllowAny]
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
                     





    


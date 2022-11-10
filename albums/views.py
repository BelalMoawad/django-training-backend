from .models import Album
from .serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *   

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class MyResultsSetPagination(LimitOffsetPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class NewAlbumView(generics.ListAPIView, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('album_cost', 'album_name')
    pagination_class = MyResultsSetPagination
    filterset_class = AlbumFilter
    def get_queryset(self):
        queryset = Album.objects.all()
        approved = self.request.query_params.get('approved')
        if approved is not None:
            queryset = queryset.filter(approved=approved)  
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AlbumView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        allAlbums = Album.objects.all()
        serializer = AlbumSerializer(allAlbums, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


class AlbumView(generics.ListAPIView, mixins.CreateModelMixin, generics.GenericAPIView):
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


class ManualAlbumView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def costStateIsValid(self, cost):
        try:
            float(cost)
        except:
            return False
        return float(cost) >= 0.0

    def get(self, request, *args, **kwargs):
        album_cost__lte = request.query_params.get('album_cost__lte') or 100000000
        album_cost__gte = request.query_params.get('album_cost__gte') or 0
        album_name = request.query_params.get('album_name') or ""
        Errors = []

        if not self.costStateIsValid(album_cost__lte) or not self.costStateIsValid(album_cost__gte):
            Errors.append("album cost must be a positive number")

        if Errors:
            return Response(
                {"Errors": Errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        album_cost__lte = float(album_cost__lte)
        album_cost__gte = float(album_cost__gte)    

        self.queryset = self.queryset.filter(
                            album_cost__gte=album_cost__gte,
                            album_cost__lte=album_cost__lte,
                            album_name__icontains=album_name
                        )
        return self.list(request)
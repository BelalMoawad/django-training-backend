from django_filters import rest_framework as filters
from .models import Album


class AlbumFilter(filters.FilterSet):
    album_cost__gte = filters.NumberFilter(field_name="album_cost", lookup_expr='gte')
    album_cost__lte = filters.NumberFilter(field_name="album_cost", lookup_expr='lte')
    album_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Album
        fields = ['album_cost', 'album_name']
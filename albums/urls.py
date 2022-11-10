from django.urls import path
from . import views


urlpatterns = [
    path('', views.AlbumView.as_view(), name='albums'),
    path('new/', views.NewAlbumView.as_view(), name = 'new_album_view')
]
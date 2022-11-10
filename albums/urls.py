from django.urls import path
from . import views


urlpatterns = [
    path('', views.AlbumView.as_view(), name='albums'),
    path('manual/', views.ManualAlbumView.as_view(), name = 'manul_albums')
]
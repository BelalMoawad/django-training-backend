from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistsView.as_view(), name = 'artists'),
    path('<int:pk>/', views.ArtistView.as_view(), name = "artist")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistsView.as_view()),
    path('<str:id>', views.ArtistView.as_view())
]
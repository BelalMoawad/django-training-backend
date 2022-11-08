import token
from django import http
import pytest
from users.views import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

client = APIClient()

@pytest.mark.django_db
class TestAuthentication :
    def test_register_dismatching_between_repeated_password_and_password(self) :
        data = {
            "username" : "belal11",
            "email" : "belal11@belal11.com",
            "password1" : "belal11",
            "password2" : "belal22"
        }
        url = reverse('register')
        response = client.post(url, data = data, format = 'json')  
        assert response.status_code == status.HTTP_400_BAD_REQUEST 

    def test_register_with_missing_any_data(self) :
        data = {
            "username" : "belal11",
            "email" : "",
            "password1" : "belal11",
            "password2" : ""
        }
        url = reverse('register')
        response = client.post(url, data = data, format = 'json')  
        assert response.status_code == status.HTTP_400_BAD_REQUEST   

    def test_register_with_weak_password(self) :
        data = {
            "username" : "belal11",
            "email" : "belal11@belal11.com",
            "password1" : "123",
            "password2" : "123"
        }
        url = reverse('register')
        response = client.post(url, data = data, format = 'json')  
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_with_used_username(self) :
        user = User.objects.create(
            username = "belal",
            password = "12345"
        )
        data = {
            "username" : "belal",
            "email" : "belal@belal.com",
            "password1" : "12345",
            "password2" : "12345"
        }
        url = reverse('register')
        response = client.post(url, data = data, format = 'json')  
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register(self) :
        data = {
            "username" : "belal11",
            "email" : "belal11@belal11.com",
            "password1" : "belal11",
            "password2" : "belal11"
        }
        url = reverse('register')
        response = client.post(url, data = data, format = 'json')  
        assert response.status_code == status.HTTP_200_OK

    def test_login(self) :
        user = User.objects.create(
            username = "belal11",
            password = "12345"
        )
        data = {
            "username" : "belal11",
            "password" : "12345"
        }
        url = reverse('login_name')
        response = client.post(url, data = data, format = 'json') 
        assert response.status_code == status.HTTP_200_OK    


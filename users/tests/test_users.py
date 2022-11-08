from rest_framework.test import APIClient
import pytest
from users.models import User
from django.urls import reverse



@pytest.mark.django_db
class TestCreateUser:
    #AAA (Arrange, Act, Asssert)
    def test_get_user(self) :
        user = User.objects.create(
            username = "belal",
            password = "12345",
            email = "b@b.com",
            bio = "it is bio",
        )
        url = reverse('specific_user', kwargs={'pk' : user.pk})
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 200

    def test_if_user_is_not_found_return_404(self) :
        self.test_get_user()
        url = reverse('specific_user', kwargs={'pk' : 2})
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 404

    def test_put_user(self) :
        user = User.objects.create(
            username = "belal",
            email = "b@b.com",
            bio = "it is bio",
        )
        url = reverse('specific_user', kwargs={'pk' : user.pk})
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 200
        data = {
            "username" : "belal1",
            "email" : 'b@b.com',
            "bio" : 'it is bio wow'
        }
        response = client.put(url, data=data, format = 'json')
        assert response.status_code == 202

    def test_patch_user(self) :
        user = User.objects.create(
            username = "belal",
            email = "b@b.com",
            bio = "it is bio",
        )
        url = reverse('specific_user', kwargs={'pk' : user.pk})
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 200
        data = {
            "bio" : 'I want peace'
        }
        response = client.patch(url, data=data, format = 'json')
        assert response.status_code == 202

    def test_patch_with_wrong_mail(self) :
        user = User.objects.create(
            username = "belal",
            email = "b@b.com",
            bio = "it is bio",
        )
        url = reverse('specific_user', kwargs={'pk' : user.pk})
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 200
        data = {
            "email" : 'I am email'
        }
        response = client.patch(url, data=data, format = 'json')
        assert response.status_code == 400

    def test_put_with_missing_data(self) :
        user = User.objects.create(
            username = "belal",
            email = "b@b.com",
            bio = "it is bio",
        )
        url = reverse('specific_user', kwargs={'pk' : user.pk})
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 200
        data = {
            "bio" : 'it is bio wow'
        }
        response = client.put(url, data=data, format = 'json')
        assert response.status_code == 400
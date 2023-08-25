from django.urls import reverse
from accounts.models import User, Profile
import pytest
from rest_framework.test import APIClient
from datetime import datetime


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="admin@gmail.com", password="@/232312a", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    client = APIClient()

    def test_get_post_response_200(self):
        url = reverse("blog:api_v1:post-list")
        response = self.client.get(url)
        assert response.status_code == 401

    def test_create_post_201_status(self, common_user):
        url = reverse("blog:api_v1:post-list")
        data = {
            "title": "test",
            "content": "test content",
            "status": True,
            "published_at": datetime.now(),
        }
        self.client.force_login(user=common_user)
        response = self.client.post(url, data)
        assert response.status_code == 201

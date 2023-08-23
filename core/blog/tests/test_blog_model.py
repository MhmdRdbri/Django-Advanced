from django.test import TestCase
from datetime import datetime
from ..models import Post, Category
from django.contrib.auth import get_user_model
from accounts.models import User, Profile

class TestPostModel(TestCase):
    
    def test_create_post_with_valid_data(self):
        user = User.objects.create_user(email='test@test.com', password='test')
        profile = Profile.objects.create(
            user = user,
            first_name = 'ali',
            last_name = 'ali',
            description = 'test description'
        )
        post = Post.objects.create(
            author = profile,
            title = "test",
            content = 'test content',
            status = True,
            category = None,
            published_at = datetime.now()
        )
        self.assertEqual(post.title, "test")
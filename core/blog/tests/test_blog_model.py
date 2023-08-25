from django.test import TestCase
from datetime import datetime
from ..models import Post, Category
from django.contrib.auth import get_user_model
from accounts.models import User, Profile

class TestPostModel(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='test')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'ali',
            last_name = 'ali',
            description = 'test description'
        )
    
    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = 'test content',
            status = True,
            category = None,
            published_at = datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.pk).exists())
        self.assertEqual(post.title, "test")
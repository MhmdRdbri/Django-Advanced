from datetime import datetime
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile
from blog.models import *


class TestBlogView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@test.com', password='test')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'ali',
            last_name = 'ali',
            description = 'test description'
        )
        self.post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = 'test content',
            status = True,
            category = None,
            published_at = datetime.now()
        )
        
    def test_blog_list_view(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_blog_post_detail(self):
        self.client.force_login(self.user)
        url = reverse('blog:post_detail',kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_blog_post_detail_anonymouse(self):
        url = reverse('blog:post_detail',kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
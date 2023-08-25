from django.test import TestCase, Client
from django.urls import reverse

class TestBlogView(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def test_blog_list_view(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
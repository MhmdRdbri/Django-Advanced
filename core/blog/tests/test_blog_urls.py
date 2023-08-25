from django.test import TestCase
from django.urls import resolve, reverse
from ..views import *

# Create your tests here.


class TestUrl(TestCase):
    def test_blog_post_list_url_resolve(self):
        url = reverse("blog:post_list")
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_blog_index_url_resolve(self):
        url = reverse("blog:post_detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

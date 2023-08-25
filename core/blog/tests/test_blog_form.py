from datetime import datetime
from django.test import SimpleTestCase, TestCase
from ..models import Category
from ..forms import *


class TestPostForm(TestCase):
    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name="Hello")
        form = PostForm(
            data={
                "title": "Test",
                "content": "Test Form",
                "status": True,
                "category": category_obj,
                "published_at": datetime.now(),
            }
        )
        self.assertTrue(form.is_valid())

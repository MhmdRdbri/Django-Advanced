from rest_framework import serializers
from blog.models import *

class postSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'snippet', 'category', 'status', 'relative_url', 'created_at', 'published_at']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
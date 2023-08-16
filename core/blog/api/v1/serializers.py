from rest_framework import serializers
from blog.models import *

class postSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'category', 'status', 'created_at', 'published_at']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
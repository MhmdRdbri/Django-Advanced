from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'image', 'title', 'content', 'status', 'category', 'created_at', 'published_at']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)

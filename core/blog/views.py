from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


class PostListView(ListView):
    model = Post
    context_object_name = "posts"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"


class PostDetailView(DetailView):
    model = Post

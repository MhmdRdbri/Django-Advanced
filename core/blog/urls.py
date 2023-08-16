from django.urls import include, path

from . import views
app_name = 'blog'
urlpatterns = [
    # path('', views.indexview, name='fbv_test'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('api/v1/', include('blog.api.v1.urls')),
]


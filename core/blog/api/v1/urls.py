from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls

app_name = 'api_v1'

# urlpatterns = [
#     # path('post/<int:id>/', views.postDetail, name='post-detail'),
#     # path('post/', views.postList, name='post-list'),
#     path('post/', views.PostList.as_view(), name='post-list'),
#     path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
# ]


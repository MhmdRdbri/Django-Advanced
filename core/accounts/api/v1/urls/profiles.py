from django.urls import include, path
from .. import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView

# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [path("", views.ProfileApiView.as_view(), name="profile")]

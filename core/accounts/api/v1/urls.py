from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api_v1'

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
]


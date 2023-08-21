from rest_framework import generics
from .serializers import RegistrationSerializer


class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        
        return super().post(request, *args, **kwargs)
    
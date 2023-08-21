from rest_framework import serializers
from ...models import *

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password']
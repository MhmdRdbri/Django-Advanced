from rest_framework import serializers
from ...models import *

class RegistrationSerializer(serializers.ModelSerializer):
    
    class MEta:
        model = User
        fields = ['email', 'password']
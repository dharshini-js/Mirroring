from rest_framework import serializers
from login.models import login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'
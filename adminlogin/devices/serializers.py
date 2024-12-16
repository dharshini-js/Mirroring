from rest_framework import serializers
from devices.models import device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = '__all__'
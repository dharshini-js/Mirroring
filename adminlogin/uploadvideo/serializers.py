from rest_framework import serializers
from uploadvideo.models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
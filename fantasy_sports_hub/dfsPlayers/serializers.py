from rest_framework import serializers
from .models import NbaDfsPlayer


class NbaDfsPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NbaDfsPlayer
        fields = '__all__'

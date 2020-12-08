from rest_framework import serializers
from .models import NflPlayer


class NflPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NflPlayer
        fields = '__all__'

from rest_framework import serializers
from .models import NflGame


class NflGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NflGame
        fields = '__all__'

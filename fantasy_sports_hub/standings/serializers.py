from rest_framework import serializers
from .models import NflStanding


class NflStandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NflStanding
        fields = '__all__'

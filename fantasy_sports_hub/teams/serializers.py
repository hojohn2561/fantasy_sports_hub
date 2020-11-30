from rest_framework import serializers
from .models import NflTeam


class NflTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = NflTeam
        fields = '__all__'

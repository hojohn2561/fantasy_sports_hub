from rest_framework import serializers
from .models import NflTeamRegularSeasonRecord


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NflTeamRegularSeasonRecord
        fields = '__all__'

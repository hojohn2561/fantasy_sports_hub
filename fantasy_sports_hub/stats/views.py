from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NflTeamRegularSeasonRecord
from .serializers import StatsSerializer


@api_view(['GET'])
def nflTeamRegularSeasonRecord(request, season_year, season_type):
    records = NflTeamRegularSeasonRecord.objects.filter(
        season_year=season_year, season_type=season_type)
    serializer = StatsSerializer(records, many=True)  # Serializes the data
    return Response(serializer.data)

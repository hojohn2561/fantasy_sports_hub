from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response  # Django REST framework response
from .models import NflStanding
from .serializers import NflStandingSerializer


@api_view(['GET'])
def nflStandings(request, season_year):
    standings = NflStanding.objects.filter(season_year=season_year)
    serializer = NflStandingSerializer(
        standings, many=True)  # Serializes the data
    return Response(serializer.data)

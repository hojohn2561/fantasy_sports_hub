from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response  # Django REST framework response
from .models import Standing
from .serializers import StandingSerializer


@api_view(['GET'])
def nflStandings(request, season_year):
    standings = Standing.objects.filter(season_year=season_year)
    serializer = StandingSerializer(
        standings, many=True)  # Serializes the data
    return Response(serializer.data)

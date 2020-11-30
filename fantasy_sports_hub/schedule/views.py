from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response  # Django REST framework response
from .models import NflGame
from .serializers import NflGameSerializer


# Create your views here.
@api_view(['GET'])
def nflSchedule(request, season_year):
    nflGames = NflGame.objects.filter(season_year=season_year)
    serializer = NflGameSerializer(
        nflGames, many=True)  # Serializes the data
    return Response(serializer.data)

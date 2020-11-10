from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response  # Django REST framework response
from .models import Team
from .serializers import TeamSerializer

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'NFL teams': '/teams/nfl',
        'NBA teams': '/teams/nba',
    }
    return Response(api_urls)


@api_view(['GET'])
def nflTeams(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)  # Serializes the data
    return Response(serializer.data)

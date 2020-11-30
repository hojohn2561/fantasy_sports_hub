from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response  # Django REST framework response
from .models import NflTeam
from .serializers import NflTeamSerializer

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'NFL teams': '/api/teams/nfl/',
        'NFL team by team ID': '/api/teams/nfl/<team_id>',
        'NBA teams': '/api/teams/nba/',
    }
    return Response(api_urls)


@api_view(['GET'])
def nflTeams(request):
    teams = NflTeam.objects.all()
    serializer = NflTeamSerializer(teams, many=True)  # Serializes the data
    return Response(serializer.data)


@api_view(['GET'])
def nflTeamById(request, team_id):
    team = NflTeam.objects.filter(id=team_id)
    serializer = NflTeamSerializer(team, many=True)
    return Response(serializer.data)

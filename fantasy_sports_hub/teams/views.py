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
        'NFL teams': '/api/teams/nfl/',
        'NFL team by team ID': '/api/teams/nfl/<team_id>',
        'NBA teams': '/api/teams/nba/',
    }
    return Response(api_urls)


@api_view(['GET'])
def nflTeams(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)  # Serializes the data
    return Response(serializer.data)


@api_view(['GET'])
def nflTeamById(request, team_id):
    team = Team.objects.filter(id=team_id)
    serializer = TeamSerializer(team, many=True)
    return Response(serializer.data)

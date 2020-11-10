from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response  # Django REST framework response
from .models import Team
from .serializers import PlayerSerializer

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'NFL': '/nfl-players/',
        'NBA': '/nba-players/',
    }
    return Response(api_urls)

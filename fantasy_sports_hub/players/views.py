from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response  # Django REST framework response
from .serializers import NflPlayerSerializer


@api_view(['GET'])
def getNflPlayer(request):
    api_urls = {
        'NFL': '/nfl-players/'
    }
    return Response(api_urls)

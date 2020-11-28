from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response  # Django REST framework response
from .models import Schedule
from teams.serializers import Team
from .serializers import ScheduleSerializer
from teams.serializers import TeamSerializer


# Create your views here.
@api_view(['GET'])
def nflSchedule(request, season_year):
    schedule = Schedule.objects.filter(season_year=season_year)
    serializer = ScheduleSerializer(
        schedule, many=True)  # Serializes the data
    return Response(serializer.data)

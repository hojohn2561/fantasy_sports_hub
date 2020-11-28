from django.db import models
from teams.models import Team


# Create your models here.
class Schedule(models.Model):
    season_year = models.PositiveIntegerField()
    season_type = models.CharField(max_length=50)
    game_id = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    # status: scheduled, created, inprogress, halftime, complete, closed, cancelled, postponed, delayed, flex-schedule, time-tbd
    status = models.CharField(max_length=50)
    game_datetime = models.DateTimeField(blank=True, null=True)
    week_num = models.PositiveSmallIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    stadium_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    attendance = models.PositiveIntegerField(default=0)
    weather = models.CharField(max_length=100, default="")
    weather_conditions = models.CharField(max_length=100, default="")
    weather_temp = models.CharField(max_length=10, default="")
    weather_wind = models.CharField(max_length=100, default="")
    surface = models.CharField(max_length=50)
    roof_type = models.CharField(max_length=50)
    home_team_id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="home_team_id", blank=True, null=True)
    home_team_name = models.CharField(max_length=100, default="")
    home_team_alias = models.CharField(max_length=10, default="")
    away_team_id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="away_team_id", blank=True, null=True)
    away_team_name = models.CharField(max_length=100, default="")
    away_team_alias = models.CharField(max_length=10, default="")
    broadcast_network = models.CharField(max_length=50)
    home_team_points = models.PositiveSmallIntegerField(default=0)
    away_team_points = models.PositiveSmallIntegerField(default=0)
    home_team_quarter_1_points = models.PositiveSmallIntegerField(default=0)
    away_team_quarter_1_points = models.PositiveSmallIntegerField(default=0)
    home_team_quarter_2_points = models.PositiveSmallIntegerField(default=0)
    away_team_quarter_2_points = models.PositiveSmallIntegerField(default=0)
    home_team_quarter_3_points = models.PositiveSmallIntegerField(default=0)
    away_team_quarter_3_points = models.PositiveSmallIntegerField(default=0)
    home_team_quarter_4_points = models.PositiveSmallIntegerField(default=0)
    away_team_quarter_4_points = models.PositiveSmallIntegerField(default=0)

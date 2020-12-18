from django.db import models
from teams.models import NflTeam


class NflPlayer(models.Model):
    player_api_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    abbreviated_name = models.CharField(max_length=50)
    birth_date: models.DateField(blank=True, null=True)
    birth_place: models.CharField(
        max_length=100, default="", blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    position = models.CharField(max_length=25, default="")
    high_school = models.CharField(max_length=50, default="")
    college = models.CharField(max_length=50, default="")
    college_conference = models.CharField(max_length=50, default="")
    rookie_year = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, default="")
    # When a team is deleted, all its asssociated players are deleted
    current_team = models.ForeignKey(
        NflTeam, related_name="current_team", on_delete=models.CASCADE, blank=True, null=True)
    jersey_number = models.PositiveSmallIntegerField(blank=True, null=True)
    year_drafted = models.PositiveIntegerField(blank=True, null=True)
    draft_round = models.PositiveSmallIntegerField(blank=True, null=True)
    number_drafted_overall = models.PositiveIntegerField(blank=True, null=True)
    team_drafted_id = models.ForeignKey(
        NflTeam, related_name="team_drafted", on_delete=models.CASCADE, blank=True, null=True)
    team_drafted_name = models.CharField(max_length=50, default="")
    team_drafted_city = models.CharField(max_length=50, default="")
    team_drafted_alias = models.CharField(max_length=10, default="")

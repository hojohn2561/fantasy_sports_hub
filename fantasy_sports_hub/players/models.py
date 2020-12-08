from django.db import models
from teams.models import NflTeam


class NflPlayer(models.Model):
    api_player_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    abbreviated_name = models.CharField(max_length=50)
    birth_date: models.DateField()
    birth_place: models.CharField(max_length=100, default="")
    age = models.PositiveSmallIntegerField()
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    position = models.CharField(max_length=25, default="")
    high_school = models.CharField(max_length=50, default="")
    college = models.CharField(max_length=50, default="")
    college_conference = models.CharField(max_length=50, default="")
    rookie_year = models.PositiveIntegerField(blank=True, null=True)
    # When a team is deleted, all its asssociated players are deleted
    current_team = models.ForeignKey(
        NflTeam, related_name="current_team", on_delete=models.CASCADE, blank=True, null=True)
    jersey_number = models.PositiveSmallIntegerField()
    year_drafted = models.PositiveIntegerField()
    draft_round = models.PositiveSmallIntegerField()
    number_drafted = models.PositiveIntegerField()
    team_drafted_id = models.ForeignKey(
        NflTeam, related_name="team_drafted", on_delete=models.CASCADE, blank=True, null=True)
    team_drafted_name = models.CharField(max_length=50, default="")
    team_drafted_city = models.CharField(max_length=50, default="")
    team_drafted_alias = models.CharField(max_length=10, default="")

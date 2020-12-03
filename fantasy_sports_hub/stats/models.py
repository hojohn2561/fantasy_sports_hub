from django.db import models
from django.core.validators import MaxValueValidator
from teams.models import NflTeam
from standings.models import NflStanding
from schedule.models import NflGame

# Create your models here.


class NflTeamRegularSeasonRecord(models.Model):
    season_year = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    standing_id = models.ForeignKey(
        NflStanding, on_delete=models.CASCADE, related_name="standing", blank=True, null=True)


class NflGameStats(models.Model):
    game_id = models.ForeignKey(
        NflGame, on_delete=models.CASCADE, related_name="game", blank=True, null=True)
#     home_team_points = models.PositiveSmallIntegerField(default=0)
#     away_team_points = models.PositiveSmallIntegerField(default=0)
#     home_team_quarter_1_points = models.PositiveSmallIntegerField(default=0)
#     away_team_quarter_1_points = models.PositiveSmallIntegerField(default=0)
#     home_team_quarter_2_points = models.PositiveSmallIntegerField(default=0)
#     away_team_quarter_2_points = models.PositiveSmallIntegerField(default=0)
#     home_team_quarter_3_points = models.PositiveSmallIntegerField(default=0)
#     away_team_quarter_3_points = models.PositiveSmallIntegerField(default=0)
#     home_team_quarter_4_points = models.PositiveSmallIntegerField(default=0)
#     away_team_quarter_4_points = models.PositiveSmallIntegerField(default=0)

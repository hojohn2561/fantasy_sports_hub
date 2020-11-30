from django.db import models
from django.core.validators import MaxValueValidator
from teams.models import NflTeam

# Create your models here.


class NflTeamRegularSeasonRecord(models.Model):
    season_year = models.PositiveIntegerField()
    season_type = models.CharField(max_length=50)
    team_id = models.ForeignKey(
        NflTeam, on_delete=models.CASCADE, related_name="team_id", blank=True, null=True)
    win_count = models.PositiveSmallIntegerField(default=0)
    loss_count = models.PositiveSmallIntegerField(default=0)
    tie_count = models.PositiveSmallIntegerField(default=0)


# class NflGameStats(models.Model):
#     game_id = models.CharField(max_length=50)
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

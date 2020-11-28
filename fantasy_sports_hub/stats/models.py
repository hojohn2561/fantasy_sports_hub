from django.db import models
from django.core.validators import MaxValueValidator
from teams.models import Team

# Create your models here.


class NflTeamRecords(models.Model):
    season_year = models.PositiveIntegerField()
    season_type = models.CharField(max_length=50)
    team_id = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_id", blank=True, null=True)
    record_2020_win_count = models.PositiveSmallIntegerField(default=0)
    record_2020_loss_count = models.PositiveSmallIntegerField(default=0)
    record_2020_tie_count = models.PositiveSmallIntegerField(default=0)
    record_2019_win_count = models.PositiveSmallIntegerField(default=0)
    record_2019_loss_count = models.PositiveSmallIntegerField(default=0)
    record_2019_tie_count = models.PositiveSmallIntegerField(default=0)
    record_2018_win_count = models.PositiveSmallIntegerField(default=0)
    record_2018_loss_count = models.PositiveSmallIntegerField(default=0)
    record_2018_tie_count = models.PositiveSmallIntegerField(default=0)


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

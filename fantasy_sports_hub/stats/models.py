from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class NflGameStats(models.Model):
    game_id = models.CharField(max_length=50)
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

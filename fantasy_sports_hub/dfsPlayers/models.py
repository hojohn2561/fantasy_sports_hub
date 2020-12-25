from django.db import models


class NbaDfsPlayer(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, default="")
    position = models.CharField(max_length=20)
    fantasy_points_per_game = models.FloatField(default=0.0)
    games_played = models.PositiveIntegerField(default=0)
    team_alias = models.CharField(max_length=10)
    opponent_team_alias = models.CharField(max_length=10)
    injury_indicator = models.CharField(max_length=50, default="")
    injury_details = models.CharField(max_length=50, default="")
    tier = models.CharField(max_length=50, default="")
    dfs_date = models.DateTimeField(blank=True, null=True)

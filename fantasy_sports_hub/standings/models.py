from django.db import models
from django.core.validators import MaxValueValidator
from teams.models import NflTeam


class NflStanding(models.Model):
    season_year = models.PositiveIntegerField()
    league = models.CharField(max_length=50)
    team_id = models.ForeignKey(
        NflTeam, on_delete=models.CASCADE, related_name="team", blank=True, null=True)
    city = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    conference = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    conference_rank = models.PositiveIntegerField(default=0)
    division_rank = models.PositiveIntegerField(default=0)
    win_count = models.PositiveIntegerField(default=0)
    loss_count = models.PositiveIntegerField(default=0)
    tie_count = models.PositiveIntegerField(default=0)
    win_percentage = models.FloatField(default=0)
    streak_type = models.CharField(max_length=6, default="")
    streak_length = models.PositiveIntegerField(default=0)
    conference_win_count = models.PositiveIntegerField(default=0)
    conference_loss_count = models.PositiveIntegerField(default=0)
    conference_tie_count = models.PositiveIntegerField(default=0)
    non_conference_win_count = models.PositiveIntegerField(default=0)
    non_conference_loss_count = models.PositiveIntegerField(default=0)
    non_conference_tie_count = models.PositiveIntegerField(default=0)
    division_win_count = models.PositiveIntegerField(default=0)
    division_loss_count = models.PositiveIntegerField(default=0)
    division_tie_count = models.PositiveIntegerField(default=0)
    non_division_win_count = models.PositiveIntegerField(default=0)
    non_division_loss_count = models.PositiveIntegerField(default=0)
    non_division_tie_count = models.PositiveIntegerField(default=0)
    points_for = models.PositiveIntegerField(default=0)
    points_against = models.PositiveIntegerField(default=0)
    points_differential = models.IntegerField(default=0)
    home_win_count = models.PositiveIntegerField(default=0)
    home_loss_count = models.PositiveIntegerField(default=0)
    home_tie_count = models.PositiveIntegerField(default=0)
    road_win_count = models.PositiveIntegerField(default=0)
    road_loss_count = models.PositiveIntegerField(default=0)
    road_tie_count = models.PositiveIntegerField(default=0)
    #team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s standing in %s (%d)" % (self.city, self.name, self.season_year, self.id)

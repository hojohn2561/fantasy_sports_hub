from django.db import models
from teams.models import Team


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    # When a team is deleted, all its asssociated players are deleted
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE)

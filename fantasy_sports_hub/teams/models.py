from django.db import models
from colorfield.fields import ColorField

# Create your models here.


class NflTeam(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    abr = models.CharField(max_length=10)
    conference = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    league = models.CharField(max_length=50)
    primary_color = ColorField(default="#FFFFFF")
    secondary_color = ColorField(default="#FFFFFF")
    tertiary_color = ColorField(default="#FFFFFF")
    logo = models.ImageField(upload_to='nfl/logos')

    def __str__(self):
        return "%s %s" % (self.city, self.name)

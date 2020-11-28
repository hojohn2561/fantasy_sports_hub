from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'abr',
                    'conference', 'division', 'league')


admin.site.register(Team, TeamAdmin)

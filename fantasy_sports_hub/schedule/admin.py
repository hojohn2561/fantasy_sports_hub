from django.contrib import admin
from .models import NflGame


# Register your models here.
class NflGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'game_id', 'season_year', 'season_type', 'league', 'status', 'week_num', 'game_datetime',
                    'home_team_name', 'away_team_name', 'broadcast_network', 'home_team_points', 'away_team_points')


admin.site.register(NflGame, NflGameAdmin)

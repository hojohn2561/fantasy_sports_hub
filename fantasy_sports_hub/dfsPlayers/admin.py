from django.contrib import admin
from .models import NbaDfsPlayer


class NbaDfsPlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'first_name', 'last_name', 'nickname', 'position', 'team_alias', 'games_played',
                    'fantasy_points_per_game', 'opponent_team_alias', 'injury_indicator', 'injury_details', 'tier', 'dfs_date')


admin.site.register(NbaDfsPlayer, NbaDfsPlayerAdmin)

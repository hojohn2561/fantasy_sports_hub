from django.contrib import admin
from .models import NflStanding


class NflStandingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'season_year', 'league', 'conference', 'division',
                    'division_rank', 'conference_rank', 'win_count', 'loss_count', 'tie_count')


admin.site.register(NflStanding, NflStandingAdmin)

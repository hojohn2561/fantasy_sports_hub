from django.contrib import admin
from .models import Standing


class StandingAdmin(admin.ModelAdmin):
    list_display = ('name', 'season_year', 'league', 'conference', 'division',
                    'division_rank', 'conference_rank', 'win_count', 'loss_count', 'tie_count')


admin.site.register(Standing, StandingAdmin)

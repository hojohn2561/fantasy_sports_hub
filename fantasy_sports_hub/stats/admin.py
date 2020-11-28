from django.contrib import admin
from .models import NflTeamRegularSeasonRecord


class NflTeamRegularSeasonRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'season_year', 'season_type', 'team_id',
                    'win_count', 'loss_count', 'tie_count')


admin.site.register(NflTeamRegularSeasonRecord,
                    NflTeamRegularSeasonRecordAdmin)

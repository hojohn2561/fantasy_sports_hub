from django.contrib import admin
from .models import NflTeamRegularSeasonRecord


class NflTeamRegularSeasonRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'season_year', 'city', 'name', 'standing_id')


admin.site.register(NflTeamRegularSeasonRecord,
                    NflTeamRegularSeasonRecordAdmin)

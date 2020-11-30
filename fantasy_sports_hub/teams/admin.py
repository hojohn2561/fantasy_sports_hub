from django.contrib import admin
from .models import NflTeam


class NflTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'abr',
                    'conference', 'division', 'league')


admin.site.register(NflTeam, NflTeamAdmin)

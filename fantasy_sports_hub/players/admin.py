from django.contrib import admin
from .models import NflPlayer


# Register your models here.
class NflPlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_api_id', 'first_name', 'last_name',
                    'age', 'position', 'abbreviated_name')


admin.site.register(NflPlayer, NflPlayerAdmin)

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nfl/records/reg/', views.nflTeamRegularSeasonRecord,
         name="nfl-team-reg-season-record"),
    #path('nba/', views.nbaTeams, name="nba-teams")
]

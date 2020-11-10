from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('nfl/<int:season_year>', views.nflStandings, name="nfl-standings"),
    #path('nba/', views.nbaTeams, name="nba-teams")
]

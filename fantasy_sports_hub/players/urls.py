from django.urls import path
from . import views

urlpatterns = [
    path('', views.getNflPlayer, name="nfl-player")
    #path('nfl/', views.nflTeams, name="nfl-teams"),
    #path('nba/', views.nbaTeams, name="nba-teams")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="players-api-overview")
    #path('nfl/', views.nflTeams, name="nfl-teams"),
    #path('nba/', views.nbaTeams, name="nba-teams")
]

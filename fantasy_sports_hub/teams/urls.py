from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.apiOverview, name="teams-api-overview"),
    path('nfl/', views.nflTeams, name="nfl-teams"),
    #path('nba/', views.nbaTeams, name="nba-teams")
]

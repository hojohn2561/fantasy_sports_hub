from api_configration import get_team_id_by_team

nfl_schedule_django_model: str = "schedule.NflGame"
nfl_standings_django_model: str = "standings.NflStanding"
nfl_team_regular_season_record_django_model: str = "stats.NflTeamRegularSeasonRecord"


# The years to get standings data for NFL
def get_nfl_standings_years():
    return [2020, 2019, 2018, 2017, 2016, 2015, 2014]


# The years to get schedules data for NFL
def get_nfl_schedules_years():
    return [2020, 2019, 2018, 2017, 2016, 2015, 2014]


# Should be a better way to handle this. Currently multiple sources of truth for the db id.
def get_db_team_id_by_api_team_id(api_team_id: str):
    if (api_team_id == get_team_id_by_team("Cleveland Browns")):
        return 1
    elif (api_team_id == get_team_id_by_team("Baltimore Ravens")):
        return 2
    elif (api_team_id == get_team_id_by_team("Pittsburgh Steelers")):
        return 3
    elif (api_team_id == get_team_id_by_team("Cincinnati Bengals")):
        return 4
    elif (api_team_id == get_team_id_by_team("Kansas City Chiefs")):
        return 5
    elif (api_team_id == get_team_id_by_team("Oakland Raiders")):
        return 6
    elif (api_team_id == get_team_id_by_team("Los Angeles Chargers")):
        return 7
    elif (api_team_id == get_team_id_by_team("Denver Broncos")):
        return 8
    elif (api_team_id == get_team_id_by_team("Tennessee Titans")):
        return 9
    elif (api_team_id == get_team_id_by_team("Indianapolis Colts")):
        return 10
    elif (api_team_id == get_team_id_by_team("Jacksonville Jaguars")):
        return 11
    elif (api_team_id == get_team_id_by_team("Houston Texans")):
        return 12
    elif (api_team_id == get_team_id_by_team("New England Patriots")):
        return 13
    elif (api_team_id == get_team_id_by_team("New York Jets")):
        return 14
    elif (api_team_id == get_team_id_by_team("Miami Dolphins")):
        return 15
    elif (api_team_id == get_team_id_by_team("Buffalo Bills")):
        return 16
    elif (api_team_id == get_team_id_by_team("New York Giants")):
        return 17
    elif (api_team_id == get_team_id_by_team("Dallas Cowboys")):
        return 18
    elif (api_team_id == get_team_id_by_team("Washington Football Team")):
        return 19
    elif (api_team_id == get_team_id_by_team("Philadelphia Eagles")):
        return 20
    elif (api_team_id == get_team_id_by_team("San Fransisco 49ers")):
        return 21
    elif (api_team_id == get_team_id_by_team("Los Angeles Rams")):
        return 22
    elif (api_team_id == get_team_id_by_team("Seattle Seahawks")):
        return 23
    elif (api_team_id == get_team_id_by_team("Arizona Cardinals")):
        return 24
    elif (api_team_id == get_team_id_by_team("Minnesota Vikings")):
        return 25
    elif (api_team_id == get_team_id_by_team("Green Bay Packers")):
        return 26
    elif (api_team_id == get_team_id_by_team("Chicago Bears")):
        return 27
    elif (api_team_id == get_team_id_by_team("Detroit Browns")):
        return 28
    elif (api_team_id == get_team_id_by_team("Tampa Bay Buccaneers")):
        return 29
    elif (api_team_id == get_team_id_by_team("Atlanta Falcons")):
        return 30
    elif (api_team_id == get_team_id_by_team("New Orleans Saints")):
        return 31
    elif (api_team_id == get_team_id_by_team("Carolina Panthers")):
        return 32
    elif (api_team_id == get_team_id_by_team("San Diego Chargers")):
        return None
    else:
        return None

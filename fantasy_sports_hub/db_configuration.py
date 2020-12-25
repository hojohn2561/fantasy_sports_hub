import json
from api_configuration import get_team_id_by_team

nfl_schedule_django_model: str = "schedule.NflGame"
nfl_standings_django_model: str = "standings.NflStanding"
nfl_team_regular_season_record_django_model: str = "stats.NflTeamRegularSeasonRecord"
nfl_players_django_model: str = "players.NflPlayer"
nba_dfs_players_django_model: str = "dfsPlayers.NbaDfsPlayer"
nfl_teams_fixture_file_path: str = "./teams/fixtures/nfl_teams_fixture.json"


# The years to get standings data for NFL
def get_nfl_standings_years():
    return [2020, 2019, 2018, 2017, 2016, 2015, 2014]


# The years to get schedules data for NFL
def get_nfl_schedules_years():
    return [2020, 2019, 2018, 2017, 2016, 2015, 2014]


# Should be a better way to handle this. Currently multiple sources of truth for the db id.
def get_db_team_id_by_api_team_id(api_team_id: str):

    with open(nfl_teams_fixture_file_path) as teams_fixture_file:
        teams_fixture_array = json.loads(teams_fixture_file.read())

        if (api_team_id == get_team_id_by_team("Cleveland Browns")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Cleveland Browns")
        elif (api_team_id == get_team_id_by_team("Baltimore Ravens")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Baltimore Ravens")
        elif (api_team_id == get_team_id_by_team("Pittsburgh Steelers")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Pittsburgh Steelers")
        elif (api_team_id == get_team_id_by_team("Cincinnati Bengals")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Cincinnati Bengals")
        elif (api_team_id == get_team_id_by_team("Kansas City Chiefs")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Kansas City Chiefs")
        elif (api_team_id == get_team_id_by_team("Oakland Raiders")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Oakland Raiders")
        elif (api_team_id == get_team_id_by_team("Los Angeles Chargers")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Los Angeles Chargers")
        elif (api_team_id == get_team_id_by_team("Denver Broncos")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Denver Broncos")
        elif (api_team_id == get_team_id_by_team("Tennessee Titans")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Tennessee Titans")
        elif (api_team_id == get_team_id_by_team("Indianapolis Colts")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Indianapolis Colts")
        elif (api_team_id == get_team_id_by_team("Jacksonville Jaguars")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Jacksonville Jaguars")
        elif (api_team_id == get_team_id_by_team("Houston Texans")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Houston Texans")
        elif (api_team_id == get_team_id_by_team("New England Patriots")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "New England Patriots")
        elif (api_team_id == get_team_id_by_team("New York Jets")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "New York Jets")
        elif (api_team_id == get_team_id_by_team("Miami Dolphins")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Miami Dolphins")
        elif (api_team_id == get_team_id_by_team("Buffalo Bills")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Buffalo Bills")
        elif (api_team_id == get_team_id_by_team("New York Giants")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "New York Giants")
        elif (api_team_id == get_team_id_by_team("Dallas Cowboys")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Dallas Cowboys")
        elif (api_team_id == get_team_id_by_team("Washington Football Team")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Washington Football Team")
        elif (api_team_id == get_team_id_by_team("Philadelphia Eagles")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Philadelphia Eagles")
        elif (api_team_id == get_team_id_by_team("San Fransisco 49ers")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "San Fransisco 49ers")
        elif (api_team_id == get_team_id_by_team("Los Angeles Rams")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Los Angeles Rams")
        elif (api_team_id == get_team_id_by_team("Seattle Seahawks")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Seattle Seahawks")
        elif (api_team_id == get_team_id_by_team("Arizona Cardinals")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Arizona Cardinals")
        elif (api_team_id == get_team_id_by_team("Minnesota Vikings")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Minnesota Vikings")
        elif (api_team_id == get_team_id_by_team("Green Bay Packers")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Green Bay Packers")
        elif (api_team_id == get_team_id_by_team("Chicago Bears")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Chicago Bears")
        elif (api_team_id == get_team_id_by_team("Detroit Browns")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Detroit Browns")
        elif (api_team_id == get_team_id_by_team("Tampa Bay Buccaneers")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Tampa Bay Buccaneers")
        elif (api_team_id == get_team_id_by_team("Atlanta Falcons")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Atlanta Falcons")
        elif (api_team_id == get_team_id_by_team("New Orleans Saints")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "New Orleans Saints")
        elif (api_team_id == get_team_id_by_team("Carolina Panthers")):
            return get_team_id_from_teams_fixture(teams_fixture_array, "Carolina Panthers")
        elif (api_team_id == get_team_id_by_team("San Diego Chargers")):
            return None
        else:
            return None


# Helper function for get_db_team_id_by_api_team_id to get the db id (pk/primary key) for team dynamically
def get_team_id_from_teams_fixture(teams_fixture_array, team_full_name):
    for team in teams_fixture_array:
        if str("%s %s" % (team["fields"]["city"], team["fields"]["name"])):
            return team["pk"]

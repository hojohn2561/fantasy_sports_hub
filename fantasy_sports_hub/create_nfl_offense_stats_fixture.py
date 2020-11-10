import requests
import os
import json
import pprint
from configuration import get_sport_radar_api_key
from api_configration import get_nfl_2019_season_url_path, get_nfl_2020_season_stats_base_path

with open("api_config.json", 'r') as api_config_file:
    external_api_config_data = api_config_file.read()
api_config = json.loads(external_api_config_data)

# Get external API configurations from config file
nfl_2019_season_url_path: str = get_nfl_2019_season_url_path()
nfl_2020_season_stats_base_path: str = get_nfl_2020_season_stats_base_path()
api_key: str = get_sport_radar_api_key()


# Makes HTTP request to external API to get all teams' attributes
def getNflTeamsApiId():
    teams = {"teams": []}
    url: str = nfl_2019_season_url_path
    response = requests.get(url=url)
    data = response.json()

    # Loop through HTTP response to get data needed for the DB
    for conference in data["conferences"]:
        for division in conference["divisions"]:
            for team in division["teams"]:
                name: str = team["name"]
                api_id: str = team["id"]
                team_obj: object = {"name": name, "id": api_id}
                # Done parsing for necessary data, add to json
                teams["teams"].append(team_obj)
    return(teams)


def getNflTeamStats(team_id: str):
    team_stats_url = nfl_2020_season_stats_base_path + \
        team_id + "/statistics.json?api_key=" + api_key
    response = requests.get(url=team_stats_url)
    print(team_stats_url)
    return response.json()


def createNflStatsFixture():
    statsFixture: list = []
    teamsData: object = getNflTeamsApiId()
    # for team in teamsData["teams"]:
    team_id: str = teamsData["teams"][0]["id"]
    teamStats = getNflTeamStats(team_id)
    print(teamStats)
    return 1


if __name__ == "__main__":
    fixture = createNflStatsFixture()

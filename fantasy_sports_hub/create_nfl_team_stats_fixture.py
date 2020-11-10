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
nfl_2019_season_url_path: get_nfl_2019_season_url_path()
nfl_2020_season_stats_base_path: str = get_nfl_2020_season_stats_base_path()
api_key: str = get_sport_radar_api_key()
nfl_team_ids = api_config["nfl_team_ids"]


def getNflTeamStats():
    teamStats = []
    team_stats_url = nfl_2020_season_stats_base_path + \
        nfl_team_ids[0]["id"] + "/statistics.json?api_key=" + api_key
    response = requests.get(url=team_stats_url)
    data = response.json()
    games_played = int(data["record"]["games_played"])
    total_rushing_yards = int(data["record"]["rushing"]["yards"])
    print(total_rushing_yards/games_played)


def createNflStatsFixture():
    statsFixture: list = []
    teamsData: object = getNflTeamStats()
    # for team in teamsData["teams"]:
    # team_id: str = teamsData["teams"][0]["id"]
    # getNflTeamStats(team_id)


if __name__ == "__main__":
    createNflStatsFixture()

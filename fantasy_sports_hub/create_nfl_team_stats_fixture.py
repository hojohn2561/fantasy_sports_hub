import argparse
import requests
import os
import json
import pprint
from configuration import get_sport_radar_api_key
from db_configuration import nfl_team_regular_season_record_django_model


# Make external API call to get team regular season records
def getNflSchedule(year: int):
    url: str = get_nfl_reg_schedule_url_path(year)
    response = requests.get(url=url)
    print(year, response)
    data = response.json()
    return data


def createNflTeamRegularSeasonRecordsFixture(year):
    nfl_team_regular_season_record_fixture: list = []
    nfl_team_regular_season_record_model: str = nfl_team_regular_season_record_django_model
    pk: int = 1
    print("")


def createNflStatsFixture(season_years):
    for year in season_years:
        createNflTeamRegularSeasonRecordsFixture(year)
    return 1


if __name__ == "__main__":
    # Get years passed as command-line arguments if any
    parser = argparse.ArgumentParser(
        description='Get NFL team stats for specified years.')
    parser.add_argument('-y', '--years', metavar='y', type=int, nargs='+',
                        help='the year to get the schedule for')
    args = parser.parse_args()

    # This main fixture contains multiple fixtures for different stats models
    fixture = createNflStatsFixture(args.years)
    nfl_team_regular_season_record_fixture_file_name = "nfl_team_regular_season_record_fixture.json"
    print("")

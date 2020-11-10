import requests
import os
import pprint
import json
from teams.fixtureConfigs.nflTeamColors import getTeamColors

with open("api_config.json", 'r') as api_config_file:
    external_api_config_data = api_config_file.read()
api_config = json.loads(external_api_config_data)

# Get external API configurations from config file
#api_access_level: str = api_config["general"]["api_access_level"]
#nfl_api_version: str = api_config["general"]["nfl_api_version"]
#language_code: str = api_config["general"]["language_code"]
#api_key: str = api_config["general"]["api_key"]
#nfl_api_base_url: str = api_config["general"]["nfl_api_base_url"]
nfl_2019_season_url_path: str = api_config["nfl_2019_season_url_path"]


# Makes HTTP request to external API to get all teams' attributes
def getNflTeams():
    teams = {"teams": []}
    url: str = nfl_2019_season_url_path
    response = requests.get(url=url)
    data = response.json()

    # Loop through HTTP response to get data needed for the DB
    for conference in data["conferences"]:
        team_conference = conference["name"]
        for division in conference["divisions"]:
            team_division = str(division["name"]).split(" ")[1]
            for team in division["teams"]:
                name: str = team["name"]
                city: str = team["market"]
                abr: str = team["alias"]
                league: str = "NFL"
                api_id: str = team["id"]
                team_obj: object = {"name": name, "city": city, "abr": abr, "conference": team_conference,
                                    "division": team_division, "league": league, "id": api_id}
                # Done parsing for necessary data, add to json
                teams["teams"].append(team_obj)
    return(teams)


# Given a team name, get that team's colors
def getNflTeamColors(team):
    # Use imported method to get the NFL team colors from config file
    return getTeamColors()[team]


# Creates the fixture to be used to populate the NFL teams DB
def createNflTeamsFixture():
    # Don't include /media or else Django will do /media/media
    path_to_image_dir: str = "nfl/logos/"
    image_file_ext: str = ".png"
    teamsFixture: list = []
    pk: int = 1

    teamsData: object = getNflTeams()

    for team in teamsData["teams"]:
        # Get primary, secondary, and teritary color for given team name
        colors = getNflTeamColors(team["name"])
        primary_color: str = colors["primary_color"]
        secondary_color: str = colors["secondary_color"]
        tertiary_color: str = colors["tertiary_color"]
        # Django model for this fixture
        django_model: str = "teams.Team"
        # Append the team's obj to the fixture for eventual loading into the DB
        teamsFixture.append({"model": django_model,
                             "pk": pk,
                             "fields": {"name": team["name"], "city": team["city"], "abr": team["abr"],
                                        "conference": team["conference"], "division": team["division"],
                                        "league": team["league"], "primary_color": primary_color,
                                        "secondary_color": secondary_color, "tertiary_color": tertiary_color,
                                        "logo": path_to_image_dir + str(team["name"]).lower() + image_file_ext}})
        pk += 1
    return(teamsFixture)


if __name__ == "__main__":
    fixture = createNflTeamsFixture()
    fixture_file_name = "nfl_teams_fixture.json"
    # pp = pprint.PrettyPrinter(depth=4)
    # pp.pprint(fixture)

    # Create the fixture file
    with open("./teams/fixtures/" + fixture_file_name, "w") as outfile:
        json.dump(fixture, outfile, indent=4, sort_keys=True)
    # Run command to load the fixture data into the DB
    os.system('python manage.py loaddata ' + fixture_file_name)

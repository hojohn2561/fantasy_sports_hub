import requests
import os
from os import path
import pprint
import json
import time
from datetime import datetime, date
from api_configuration import get_all_team_ids, get_nfl_team_roster_url_path
from db_configuration import nfl_players_django_model, get_db_team_id_by_api_team_id


def getTeamRoster(team_id: str):
    url: str = get_nfl_team_roster_url_path(team_id)
    response = requests.get(url=url)
    print(response)
    data = response.json()
    print(data)


# Creates the fixture to be used to populate the NFL players DB
def createNflPlayersFixture():
    players_fixture: list = []
    django_model: str = nfl_players_django_model
    pk: int = 1
    team_ids = get_all_team_ids()

    for team_id in team_ids:
        team: object = getTeamRoster(team_id)
        # Making multiple API calls won't work without this timeout
        time.sleep(1)

        team_name = team["name"]
        print(team_name)
        team_city = team["market"]
        team_alias = team["alias"]
        for player in team["players"]:
            player_api_id = player["id"]
            first_name = player["first_name"]
            last_name = player["last_name"]
            abbreviated_name = player["abbr_name"]
            birth_date = ""
            age: None
            if "birth_date" in player:
                birth_date_str = player["birth_date"]
                birth_datetime = datetime.strptime(
                    birth_date_str, '%Y-%m-%d')
                age: int = calculateAge(birth_datetime)
            birth_place = ""
            if "birth_place" in player:
                birth_place = player["birth_place"]

            weight = None
            if "weight" in player:
                weight = player["weight"]

            height: None
            if "height" in player:
                height = player["height"]

            position = player["position"]
            jersey_number = player["jersey"]

            high_school = ""
            if "high_school" in player:
                high_school = player["high_school"]

            college = ""
            if "college" in player:
                college = player["college"]

            college_conference = player["college_conf"]

            rookie_year = None
            if "rookie_year" in player:
                rookie_year = player["rookie_year"]

            status = player["status"]
            # The player's current team's ID (db id)
            current_team = get_db_team_id_by_api_team_id(team_id)

            # Player might not've been drafted (i.e., signed as an undrafted free agent)
            year_drafted = None
            draft_round = None
            number_drafted_overall = None
            team_drafted_name = ""
            team_drafted_city = ""
            team_drafted_alias = ""
            team_drafted_api_id = None
            team_drafted_db_id = None
            if "draft" in player:
                try:
                    draft_data = player["draft"]
                    year_drafted = draft_data["year"]
                    draft_round = draft_data["round"]
                    number_drafted_overall = draft_data["number"]
                    team_drafted_name = draft_data["team"]["name"]
                    team_drafted_city = draft_data["team"]["market"]
                    team_drafted_alias = draft_data["team"]["alias"]
                    team_drafted_api_id = draft_data["team"]["id"]
                    # Team Id (db id) of team that drafted player
                    team_drafted_db_id = get_db_team_id_by_api_team_id(
                        team_drafted_api_id)
                except:
                    pass

            players_fixture.append({"model": django_model, "pk": pk, "fields": {"player_api_id": player_api_id, "first_name": first_name, "last_name": last_name,
                                                                                "abbreviated_name": abbreviated_name, "birth_date": birth_datetime.isoformat(), "age": age,
                                                                                "birth_place": birth_place, "weight": weight, "height": height, "position": position,
                                                                                "jersey_number": jersey_number, "high_school": high_school, "college": college,
                                                                                "college_conference": college_conference, "rookie_year": rookie_year, "status": status,
                                                                                "current_team": current_team, "year_drafted": year_drafted, "draft_round": draft_round,
                                                                                "number_drafted_overall": number_drafted_overall, "team_drafted_name": team_drafted_name,
                                                                                "team_drafted_city": team_drafted_city, "team_drafted_alias": team_drafted_alias,
                                                                                "team_drafted_id": team_drafted_db_id}})

            pk += 1

    return players_fixture


def calculateAge(dob_datetime):
    today_datetime_obj = date.today()
    age = today_datetime_obj.year - dob_datetime.year
    if today_datetime_obj.month < dob_datetime.month or (today_datetime_obj.month == dob_datetime.month and today_datetime_obj.day < dob_datetime.day):
        age -= 1
    return age


if __name__ == "__main__":
    fixture = createNflPlayersFixture()
    fixture_file_name = "nfl_players_fixture.json"

    with open("./players/fixtures/" + fixture_file_name, "w") as outfile:
        json.dump(fixture, outfile, indent=4, sort_keys=True)

    # Run command to load the fixture data into the DB
    os.system('python manage.py loaddata ' + fixture_file_name)

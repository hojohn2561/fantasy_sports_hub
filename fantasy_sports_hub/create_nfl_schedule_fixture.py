import requests
import os
import pprint
import json
import time
from datetime import datetime
from configuration import get_sport_radar_api_key
from api_configration import get_nfl_reg_schedule_url_path
from db_configuration import get_nfl_schedules_years, nfl_schedule_django_model


# Make external API call to get standings
def getNflSchedule(year: int):
    url: str = get_nfl_reg_schedule_url_path(year)
    response = requests.get(url=url)
    print(year, response)
    data = response.json()
    return data


# Creates the fixture to be used to populate the NFL schedule DB
def createNflScheduleFixture():
    scheduleFixture: list = []
    # Django model for this fixture
    django_model: str = nfl_schedule_django_model
    pk: int = 1

    # Years to get schedules for
    schedule_years = get_nfl_schedules_years()

    for year in schedule_years:
        schedule_data: object = getNflSchedule(year)
        time.sleep(1)
        season_year = schedule_data["year"]
        season_type = schedule_data["type"]
        league = "NFL"
        week: int = 1  # Each year's regular season schedule starts with week 1
        for week in schedule_data["weeks"]:
            week_num = week["sequence"]

            for game in week["games"]:
                game_id = game["id"]
                status = game["status"]

                game_datetime = game["scheduled"]

                # Only exists if game has been played already
                attendance = 0
                if "attendance" in game:
                    attendance = game["attendance"]

                # Only exists if game has been played already
                # Sportradar API weather attributes are a bit inconsistent
                weather = ""
                if "weather" in game:
                    weather = game["weather"]
                    # Capitalize every first word
                    weather_conditions = weather.split(
                        "Temp: ")[0].title().strip()
                    weather_temp = weather.split(
                        "Temp: ")[1].split(",")[0].strip()
                    weather_wind = "N/A"
                    try:
                        wind_mph = weather.split("Wind:")[1].split(" ")[2]
                        if not wind_mph.isnumeric():
                            weather_wind = "N/A"
                        else:
                            weather_wind = wind_mph + " MPH"
                    except:
                        pass
                    print(weather_conditions, weather_temp, weather.split(
                        "Wind:")[1].split(" "))

                city = game["venue"]["city"]

                state = ""
                if "state" in game["venue"]:
                    state = game["venue"]["state"]

                venue_obj = game["venue"]
                country = venue_obj["country"]

                zip_code = 0
                if "zip" in venue_obj:
                    try:
                        zip_code = int(venue_obj["zip"])
                    except:
                        zip_code = 0

                address = venue_obj["address"]
                stadium_name = venue_obj["name"]
                capacity = venue_obj["capacity"]
                surface = venue_obj["surface"]
                roof_type = venue_obj["roof_type"]

                home_obj = game["home"]
                home_team_name = home_obj["name"]
                home_team_alias = home_obj["alias"]

                away_obj = game["away"]
                away_team_name = away_obj["name"]
                away_team_alias = away_obj["alias"]

                # May not exist if undecided
                broadcast_network = "TBA"
                if "broadcast" in game:
                    broadcast_network = game["broadcast"]["network"]

                # Will only exist if game has concluded/in progress
                home_team_points = 0
                away_team_points = 0
                home_team_quarter_1_points = 0
                away_team_quarter_1_points = 0
                home_team_quarter_2_points = 0
                away_team_quarter_2_points = 0
                home_team_quarter_3_points = 0
                away_team_quarter_3_points = 0
                home_team_quarter_4_points = 0
                away_team_quarter_4_points = 0
                if "scoring" in game:
                    scoring_obj = game["scoring"]
                    home_team_points = scoring_obj["home_points"]
                    away_team_points = scoring_obj["away_points"]
                    for period in scoring_obj["periods"]:
                        quarter_number = period["number"]
                        if quarter_number == 1:
                            home_team_quarter_1_points = period["home_points"]
                            away_team_quarter_1_points = period["away_points"]
                        elif quarter_number == 2:
                            home_team_quarter_2_points = period["home_points"]
                            away_team_quarter_2_points = period["away_points"]
                        elif quarter_number == 3:
                            home_team_quarter_3_points = period["home_points"]
                            away_team_quarter_3_points = period["away_points"]
                        elif quarter_number == 4:
                            home_team_quarter_4_points = period["home_points"]
                            away_team_quarter_4_points = period["away_points"]

                scheduleFixture.append(
                    {"model": django_model, "pk": pk, "fields": {"season_year": season_year, "season_type": season_type, "league": league, "game_id": game_id, "status": status,
                                                                 "game_datetime": game_datetime, "week_num": week_num, "city": city, "state": state, "country": country, "zip_code": zip_code,
                                                                 "address": address, "stadium_name": stadium_name, "capacity": capacity, "attendance": attendance, "weather": weather,
                                                                 "weather_conditions": weather_conditions, "weather_temp": weather_temp, "weather_wind": weather_wind, "surface": surface,
                                                                 "roof_type": roof_type, "home_team_name": home_team_name, "home_team_alias": home_team_alias, "away_team_name": away_team_name,
                                                                 "away_team_alias": away_team_alias, "broadcast_network": broadcast_network, "home_team_quarter_1_points": home_team_quarter_1_points,
                                                                 "away_team_quarter_1_points": away_team_quarter_1_points, "home_team_quarter_2_points": home_team_quarter_2_points,
                                                                 "away_team_quarter_2_points": away_team_quarter_2_points, "home_team_quarter_3_points": home_team_quarter_3_points,
                                                                 "away_team_quarter_3_points": away_team_quarter_3_points, "home_team_quarter_4_points": home_team_quarter_4_points,
                                                                 "away_team_quarter_4_points": away_team_quarter_4_points, "home_team_points": home_team_points, "away_team_points": away_team_points}})
                pk += 1

    return scheduleFixture


if __name__ == "__main__":
    fixture = createNflScheduleFixture()
    fixture_file_name = "nfl_schedule_fixture.json"
    # pp = pprint.PrettyPrinter(depth=4)
    # pp.pprint(fixture)

    # Create the fixture file
    with open("./schedule/fixtures/" + fixture_file_name, "w") as outfile:
        json.dump(fixture, outfile, indent=4, sort_keys=True)
    # Run command to load the fixture data into the DB
    os.system('python manage.py loaddata ' + fixture_file_name)

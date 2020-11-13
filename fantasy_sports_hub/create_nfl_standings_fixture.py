import requests
import os
import json
import time
from configuration import get_sport_radar_api_key
from api_configration import get_nfl_standings_url_path
from db_configuration import get_nfl_standings_years, nfl_standings_django_model


# Make external API call to get standings
def getNflStandings(year: int):
    url: str = get_nfl_standings_url_path(year)
    response = requests.get(url=url)
    print(year, response)
    data = response.json()
    return data


def createNflStandingsFixture():
    standingsFixture: list = []
    django_model: str = nfl_standings_django_model
    pk: int = 1

    # Years to get standings for
    standings_years = get_nfl_standings_years()

    for year in standings_years:
        standings_data: object = getNflStandings(year)
        # Making multiple API calls won't work without this timeout
        time.sleep(1)
        season_year = standings_data["season"]["year"]

        for conference in standings_data["conferences"]:
            cur_conference = conference["name"]
            for division in conference["divisions"]:
                cur_division = division["name"]
                for team in division["teams"]:
                    # Parse to get only needed data
                    name = team["name"]
                    city = team["market"]
                    win_count = team["wins"]
                    loss_count = team["losses"]
                    tie_count = team["ties"]
                    win_percentage = float(team["win_pct"])
                    points_for = team["points_for"]
                    points_against = team["points_against"]
                    points_differential = points_for - points_against
                    division_rank = team["rank"]["division"]
                    conference_rank = team["rank"]["conference"]
                    streak_type = team["streak"]["type"]
                    # Shorten streak type to just a letter
                    if streak_type == "win":
                        streak_type = "W"
                    elif streak_type == "loss":
                        streak_type = "L"
                    elif streak_type == "tie":
                        streak_type = "T"
                    streak_length = team["streak"]["length"]
                    # Go through nested JSON element to get record values
                    for records in team["records"]:
                        cur_record_section = records["record"]
                        current_record_category = cur_record_section["category"]
                        if (cur_conference.lower() == current_record_category):
                            conference_win_count = cur_record_section["wins"]
                            conference_loss_count = cur_record_section["losses"]
                            conference_tie_count = cur_record_section["ties"]
                        elif (current_record_category == "division"):
                            division_win_count = cur_record_section["wins"]
                            division_loss_count = cur_record_section["losses"]
                            division_tie_count = cur_record_section["ties"]
                            non_division_win_count = win_count - division_win_count
                            non_division_loss_count = loss_count - division_loss_count
                            non_division_tie_count = tie_count - division_tie_count
                        elif (current_record_category == "home"):
                            home_win_count = cur_record_section["wins"]
                            home_loss_count = cur_record_section["losses"]
                            home_tie_count = cur_record_section["ties"]
                        elif (current_record_category == "road"):
                            road_win_count = cur_record_section["wins"]
                            road_loss_count = cur_record_section["losses"]
                            road_tie_count = cur_record_section["ties"]
                        elif (current_record_category == "afc"):
                            if (cur_conference.lower() == "nfc"):
                                non_conference_win_count = cur_record_section["wins"]
                                non_conference_loss_count = cur_record_section["losses"]
                                non_conference_tie_count = cur_record_section["ties"]
                        elif (current_record_category == "nfc"):
                            if (cur_conference.lower() == "afc"):
                                non_conference_win_count = cur_record_section["wins"]
                                non_conference_loss_count = cur_record_section["losses"]
                                non_conference_tie_count = cur_record_section["ties"]
                    # Append data to JSON response for our API
                    standingsFixture.append(
                        {"model": django_model, "pk": pk, "fields": {"season_year": season_year, "league": "NFL", "conference": cur_conference, "division": cur_division, "name": name, "city": city,
                                                                     "win_count": win_count, "loss_count": loss_count, "tie_count": tie_count, "win_percentage": win_percentage,
                                                                     "points_for": points_for, "points_against": points_against, "points_differential": points_differential,
                                                                     "division_rank": division_rank, "conference_rank": conference_rank, "streak_type": streak_type, "streak_length": streak_length,
                                                                     "conference_win_count": conference_win_count, "conference_loss_count": conference_loss_count, "conference_tie_count": conference_tie_count,
                                                                     "non_conference_win_count": non_conference_win_count, "non_conference_loss_count": non_conference_loss_count, "non_conference_tie_count": non_conference_tie_count,
                                                                     "division_win_count": division_win_count, "division_loss_count": division_loss_count, "division_tie_count": division_tie_count,
                                                                     "non_division_win_count": non_division_win_count, "non_division_loss_count": non_division_loss_count, "non_division_tie_count": non_division_tie_count,
                                                                     "home_win_count": home_win_count, "home_loss_count": home_loss_count, "home_tie_count": home_tie_count,
                                                                     "road_win_count": road_win_count, "road_loss_count": road_loss_count, "road_tie_count": road_tie_count}})
                    pk += 1
    return (standingsFixture)


if __name__ == "__main__":
    fixture = createNflStandingsFixture()
    fixture_file_name = "nfl_standings_fixture.json"

    # Create the fixture file
    with open("./standings/fixtures/" + fixture_file_name, "w") as outfile:
        json.dump(fixture, outfile, indent=4, sort_keys=True)
    # Run command to load the fixture data into the DB
    os.system('python manage.py loaddata ' + fixture_file_name)

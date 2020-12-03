import json
from configuration import get_sport_radar_api_key

nfl_api_base_url = "https://api.sportradar.us/nfl/official"
access_level = "trial"
api_version = "v6"
english_lang_code = "en"
browns_api_id = "d5a2eb42-8065-4174-ab79-0a6fa820e35e"
ravens_api_id = "ebd87119-b331-4469-9ea6-d51fe3ce2f1c"
steelers_api_id = "cb2f9f1f-ac67-424e-9e72-1475cb0ed398"
bengals_api_id = "ad4ae08f-d808-42d5-a1e6-e9bc4e34d123"
chiefs_api_id = "6680d28d-d4d2-49f6-aace-5292d3ec02c2"
raiders_api_id = "1c1cec48-6352-4556-b789-35304c1a6ae1"
chargers_api_id = "1f6dcffb-9823-43cd-9ff4-e7a8466749b5"
broncos_api_id = "ce92bd47-93d5-4fe9-ada4-0fc681e6caa0"
titans_api_id = "d26a1ca5-722d-4274-8f97-c92e49c96315"
colts_api_id = "82cf9565-6eb9-4f01-bdbd-5aa0d472fcd9"
jaguars_api_id = "f7ddd7fa-0bae-4f90-bc8e-669e4d6cf2de"
texans_api_id = "82d2d380-3834-4938-835f-aec541e5ece7"
patriots_api_id = "97354895-8c77-4fd4-a860-32e62ea7382a"
jets_api_id = "5fee86ae-74ab-4bdd-8416-42a9dd9964f3"
dolphins_api_id = "4809ecb0-abd3-451d-9c4a-92a90b83ca06"
bills_api_id = "768c92aa-75ff-4a43-bcc0-f2798c2e1724"
giants_api_id = "04aa1c9d-66da-489d-b16a-1dee3f2eec4d"
cowboys_api_id = "e627eec7-bbae-4fa4-8e73-8e1d6bc5c060"
football_team_api_id = "22052ff7-c065-42ee-bc8f-c4691c50e624"
eagles_api_id = "386bdbf9-9eea-4869-bb9a-274b0bc66e80"
fourty_niners_api_id = "f0e724b0-4cbf-495a-be47-013907608da9"
rams_api_id = "2eff2a03-54d4-46ba-890e-2bc3925548f3"
seahawks_api_id = "3d08af9e-c767-4f88-a7dc-b920c6d2b4a8"
cardinals_api_id = "de760528-1dc0-416a-a978-b510d20692ff"
vikings_api_id = "33405046-04ee-4058-a950-d606f8c30852"
packers_api_id = "a20471b4-a8d9-40c7-95ad-90cc30e46932"
bears_api_id = "7b112545-38e6-483c-a55c-96cf6ee49cb8"
lions_api_id = "c5a59daa-53a7-4de0-851f-fb12be893e9e"
buccaneers_api_id = "4254d319-1bc7-4f81-b4ab-b5e6f3402b69"
falcons_api_id = "e6aa13a4-0055-48a9-bc41-be28dc106929"
saints_api_id = "0d855753-ea21-4953-89f9-0e20aff9eb73"
panthers_api_id = "f14bf5cc-9a82-4a38-bc15-d39f75ed5314"


def get_nfl_2019_season_url_path():
    return nfl_api_base_url + "/" + access_level + "/" + api_version + "/" + english_lang_code + "/" + "seasons/2019/REG/standings/season.json?api_key=" + get_sport_radar_api_key()


def get_nfl_2020_season_url_path():
    return nfl_api_base_url + "/" + access_level + "/" + api_version + "/" + english_lang_code + "/" + "seasons/2020/REG/standings/season.json?api_key=" + get_sport_radar_api_key()


def get_nfl_2020_season_stats_base_path():
    return nfl_api_base_url + "/" + access_level + "/" + api_version + "/" + english_lang_code + "/" + "seasons/2020/REG/teams/"


def get_nfl_standings_url_path(year: int):
    return nfl_api_base_url + "/" + access_level + "/" + api_version + "/" + english_lang_code + "/seasons/" + str(year) + "/standings.json?api_key=" + get_sport_radar_api_key()


def get_nfl_reg_schedule_url_path(year: int):
    return nfl_api_base_url + "/" + access_level + "/" + api_version + "/" + english_lang_code + "/games/" + str(year) + "/REG/schedule.json?api_key=" + get_sport_radar_api_key()


def get_nfl_game_statistics(game_id: str):
    return nfl_api_base_url + "/" + access_level + "/" + api_version + "/" + english_lang_code + "/games/" + game_id + "/statistics.json?api_key=" + get_sport_radar_api_key()


def get_all_team_ids():
    return [browns_api_id, ravens_api_id, steelers_api_id, bengals_api_id, chiefs_api_id, raiders_api_id, chargers_api_id, broncos_api_id,
            titans_api_id, colts_api_id, jaguars_api_id, texans_api_id, patriots_api_id, jets_api_id, dolphins_api_id, bills_api_id,
            giants_api_id, cowboys_api_id, football_team_api_id, eagles_api_id, fourty_niners_api_id, rams_api_id, seahawks_api_id, cardinals_api_id,
            vikings_api_id, packers_api_id, bears_api_id, lions_api_id, buccaneers_api_id, falcons_api_id, saints_api_id, panthers_api_id]


def get_team_id_by_team(team_city_and_name: str):
    # Current team names
    if (team_city_and_name == "Cleveland Browns"):
        return browns_api_id
    elif (team_city_and_name == "Baltimore Ravens"):
        return ravens_api_id
    elif (team_city_and_name == "Pittsurgh Steelers"):
        return steelers_api_id
    elif (team_city_and_name == "Cincinnati Bengals"):
        return bengals_api_id
    elif (team_city_and_name == "Kansas City Chiefs"):
        return chiefs_api_id
    elif (team_city_and_name == "Oakland Raiders"):
        return raiders_api_id
    elif (team_city_and_name == "Los Angeles Chargers"):
        return chargers_api_id
    elif (team_city_and_name == "Denver Broncos"):
        return broncos_api_id
    elif (team_city_and_name == "Tennessee Titans"):
        return titans_api_id
    elif (team_city_and_name == "Indianapolis Colts"):
        return colts_api_id
    elif (team_city_and_name == "Jacksonville Jaguars"):
        return jaguars_api_id
    elif (team_city_and_name == "Houston Texans"):
        return texans_api_id
    elif (team_city_and_name == "New England Patriots"):
        return patriots_api_id
    elif (team_city_and_name == "New York Jets"):
        return jets_api_id
    elif (team_city_and_name == "Miami Dolphins"):
        return dolphins_api_id
    elif (team_city_and_name == "Buffalo Bills"):
        return bills_api_id
    elif (team_city_and_name == "New York Giants"):
        return giants_api_id
    elif (team_city_and_name == "Dallas Cowboys"):
        return cowboys_api_id
    elif (team_city_and_name == "Washington Football Team"):
        return football_team_api_id
    elif (team_city_and_name == "Philadelphia Eagles"):
        return eagles_api_id
    elif (team_city_and_name == "San Fransisco 49ers"):
        return fourty_niners_api_id
    elif (team_city_and_name == "Los Angeles Rams"):
        return rams_api_id
    elif (team_city_and_name == "Seattle Seahawks"):
        return seahawks_api_id
    elif (team_city_and_name == "Arizona Cardinals"):
        return cardinals_api_id
    elif (team_city_and_name == "Minnesota Vikings"):
        return vikings_api_id
    elif (team_city_and_name == "Green Bay Packers"):
        return packers_api_id
    elif (team_city_and_name == "Chicago Bears"):
        return bears_api_id
    elif (team_city_and_name == "Detriot Lions"):
        return lions_api_id
    elif (team_city_and_name == "Tampa Bay Buccaneers"):
        return buccaneers_api_id
    elif (team_city_and_name == "Atlanta Falcons"):
        return falcons_api_id
    elif (team_city_and_name == "New Orleans Saints"):
        return saints_api_id
    elif (team_city_and_name == "Carolina Panthers"):
        return panthers_api_id
    # Past team names
    elif (team_city_and_name == "San Diego Chargers"):
        return "9dbb9060-ba0f-4920-829e-16d4d9246b5d"
    else:
        return {"id": None, "name": None}

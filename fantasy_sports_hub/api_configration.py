import json
from configuration import get_sport_radar_api_key

nfl_api_base_url = "https://api.sportradar.us/nfl/official"
access_level = "trial"
api_version = "v6"
english_lang_code = "en"


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

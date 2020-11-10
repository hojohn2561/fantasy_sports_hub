from configuration import get_sport_radar_api_key


def get_nfl_2019_season_url_path():
    return "https://api.sportradar.us/nfl/official/trial/v6/en/seasons/2019/REG/standings/season.json?api_key=" + get_sport_radar_api_key()


def get_nfl_2020_standings_url_path():
    return "https://api.sportradar.us/nfl/official/trial/v6/en/seasons/2020/standings.json?api_key=" + get_sport_radar_api_key()


def get_nfl_2020_season_stats_base_path():
    return "https://api.sportradar.us/nfl/official/trial/v6/en/seasons/2020/REG/teams/"

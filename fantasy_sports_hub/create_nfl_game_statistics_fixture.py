import argparse
import requests
import os
import json
import time
from api_configuration import get_nfl_game_statistics


def getNflGameStatistics():
    game_id = ""
    url: str = get_nfl_game_statistics(game_id)
    response = requests.get(url=url)
    return 1


def createNflGamesStatisticsFixture():
    schedule_data: object = getNflGameStatistics()


if __name__ == "__main__":
    createNflGamesStatisticsFixture()

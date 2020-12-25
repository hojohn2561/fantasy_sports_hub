import argparse
import os
import json
import csv
from datetime import datetime
from db_configuration import nba_dfs_players_django_model

# The template csv file containing just the player data
TEMPLATE_FILENAME = "FanDuel-NBA-2020-12-25-52716-entries-upload-template.csv"
DFS_DATE = datetime(2020, 12, 25, 0, 0).isoformat()


def pretty_print_player_data(player_data_dict):
    for key in player_data_dict:
        print(f'\t{key}: {player_data_dict[key]}')


def create_player_data_dict(player_data_csv_file):
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    # Dictionary that will hold the organized data. Each column is a key, whose value is an array.
    # Using an index, you can get a particular player's info.
    player_data = {}

    for row in csv_reader:
        # If first line in csv, use columns to create the keys for the dictionary
        if line_count == 0:
            for column in row:
                # Don't need Player ID, so just take it out of the key
                if column == 'Player ID + Player Name':
                    temp = 'Player Name'
                    player_data[temp] = []
                elif column != 'Id':
                    player_data[column] = []
        # Otherwise, not first line in csv, so populate the dictionary keys with the list values
        else:
            player_data['Player Name'].append(row[0].split(':')[1])
            player_data['Position'].append(row[2])
            player_data['First Name'].append(row[3])
            player_data['Nickname'].append(row[4])
            player_data['Last Name'].append(row[5])
            player_data['FPPG'].append(row[6])
            player_data['Played'].append(row[7])
            player_data['Salary'].append(row[8])
            player_data['Game'].append(row[9])
            player_data['Team'].append(row[10])
            player_data['Opponent'].append(row[11])
            player_data['Injury Indicator'].append(row[12])
            player_data['Injury Details'].append(row[13])
            player_data['Tier'].append(row[14])

        line_count += 1
    #print(f'Processed {line_count} lines.')
    # print(player_data)
    return player_data


def createNbaDfsPlayersFixture(player_data_dict):
    num_of_players: int = len(player_data_dict['Player Name'])
    nbaDfsPlayersFixture: list = []
    django_model: str = nba_dfs_players_django_model
    pk: int = 1

    for i in range(0, num_of_players):
        name = player_data_dict['Player Name'][i]
        first_name = player_data_dict['First Name'][i]
        last_name = player_data_dict['Last Name'][i]
        nickname = player_data_dict['Nickname'][i]
        position = player_data_dict['Position'][i]

        fantasy_points_per_game = 0
        if player_data_dict['FPPG'][i] != '':
            fantasy_points_per_game = round(
                float(player_data_dict['FPPG'][i]), 2)

        games_played = 0
        if player_data_dict['Played'][i] != '':
            games_played = int(player_data_dict['Played'][i])

        team_alias = player_data_dict['Team'][i]
        opponent_team_alias = player_data_dict['Opponent'][i]
        injury_indicator = player_data_dict['Injury Indicator'][i]
        injury_details = player_data_dict['Injury Details'][i]
        tier = player_data_dict['Tier'][i]

        nbaDfsPlayersFixture.append(
            {"model": django_model, "pk": pk, "fields": {"name": name, "first_name": first_name, "last_name": last_name, "nickname": nickname, "position": position,
                                                         "fantasy_points_per_game": fantasy_points_per_game, "games_played": games_played, "team_alias": team_alias,
                                                         "opponent_team_alias": opponent_team_alias, "injury_indicator": injury_indicator, "injury_details": injury_details,
                                                         "tier": tier, "dfs_date": DFS_DATE}})
        pk += 1

    return nbaDfsPlayersFixture


if __name__ == "__main__":
    # Open the csv file and parse it to organize the data
    with open(TEMPLATE_FILENAME) as csv_file:
        player_data_dict = create_player_data_dict(csv_file)
        # pretty_print_player_data(player_data_dict)
        fixture = createNbaDfsPlayersFixture(player_data_dict)

        fixture_file_name = "nba_dfs_players_fixture.json"

        # Create the fixture file
        with open("./dfsPlayers/fixtures/" + fixture_file_name, "w") as outfile:
            json.dump(fixture, outfile, indent=4, sort_keys=True)
            # Run command to load the fixture data into the DB
            os.system('python manage.py loaddata ' + fixture_file_name)
            # Manual command, works for some reason, but os line above doesn't
            # python manage.py loaddata ./dfsPlayers/fixtures/nba_dfs_players_fixture.json

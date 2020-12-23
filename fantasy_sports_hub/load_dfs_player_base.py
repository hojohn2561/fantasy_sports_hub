import argparse
import os
import csv


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


if __name__ == "__main__":
    # The template csv file containing just the player data
    template_filename = "FanDuel-NBA-2020-12-22-52500-entries-upload-template.csv"

    # Open the csv file and parse it to organize the data
    with open(template_filename) as csv_file:
        player_data_dict = create_player_data_dict(csv_file)
        pretty_print_player_data(player_data_dict)

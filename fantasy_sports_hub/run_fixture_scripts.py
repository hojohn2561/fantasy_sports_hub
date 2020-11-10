import os

nfl_teams_fixture_file_name = "nfl_teams_fixture.json"
nfl_standings_fixture_file_name = "nfl_standings_fixture.json"

os.system('python manage.py loaddata ' + nfl_teams_fixture_file_name)
os.system('python manage.py loaddata ' + nfl_standings_fixture_file_name)

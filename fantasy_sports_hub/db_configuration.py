nfl_schedule_django_model: str = "schedule.Schedule"
nfl_standings_django_model: str = "standings.Standing"


# The years to get standings data for NFL
def get_nfl_standings_years():
    return [2020, 2019, 2018, 2017, 2016, 2015, 2014]


# The years to get schedules data for NFL
def get_nfl_schedules_years():
    return [2020]

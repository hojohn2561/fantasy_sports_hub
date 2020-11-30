nfl_schedule_django_model: str = "schedule.NflGame"
nfl_standings_django_model: str = "standings.Standing"
nfl_team_regular_season_record_django_model: str = "stats.NflTeamRegularSeasonRecord"


# The years to get standings data for NFL
def get_nfl_standings_years():
    return [2020, 2019, 2018, 2017, 2016, 2015, 2014]


# The years to get schedules data for NFL
def get_nfl_schedules_years():
    return [2020, 2019, 2018, 2017, 2016, 2015, 2014]


# Should be a better way to handle this. Currently multiple sources of truth for the db id.
def get_db_team_id_by_api_team_id(api_team_id: str):
    if (api_team_id == "d5a2eb42-8065-4174-ab79-0a6fa820e35e"):
        return {"id": 1, "name": "Browns"}
    elif (api_team_id == "ebd87119-b331-4469-9ea6-d51fe3ce2f1c"):
        return {"id": 2, "name": "Ravens"}
    elif (api_team_id == "cb2f9f1f-ac67-424e-9e72-1475cb0ed398"):
        return {"id": 3, "name": "Steelers"}
    elif (api_team_id == "ad4ae08f-d808-42d5-a1e6-e9bc4e34d123"):
        return {"id": 4, "name": "Bengals"}
    elif (api_team_id == "6680d28d-d4d2-49f6-aace-5292d3ec02c2"):
        return {"id": 5, "name": "Chiefs"}
    elif (api_team_id == "1c1cec48-6352-4556-b789-35304c1a6ae1"):
        return {"id": 6, "name": "Raiders"}
    elif (api_team_id == "1f6dcffb-9823-43cd-9ff4-e7a8466749b5"):
        return {"id": 7, "name": "Chargers"}
    elif (api_team_id == "ce92bd47-93d5-4fe9-ada4-0fc681e6caa0"):
        return {"id": 8, "name": "Broncos"}
    elif (api_team_id == "d26a1ca5-722d-4274-8f97-c92e49c96315"):
        return {"id": 9, "name": "Titans"}
    elif (api_team_id == "82cf9565-6eb9-4f01-bdbd-5aa0d472fcd9"):
        return {"id": 10, "name": "Colts"}
    elif (api_team_id == "f7ddd7fa-0bae-4f90-bc8e-669e4d6cf2de"):
        return {"id": 11, "name": "Jaguars"}
    elif (api_team_id == "82d2d380-3834-4938-835f-aec541e5ece7"):
        return {"id": 12, "name": "Texans"}
    elif (api_team_id == "97354895-8c77-4fd4-a860-32e62ea7382a"):
        return {"id": 13, "name": "Patriots"}
    elif (api_team_id == "5fee86ae-74ab-4bdd-8416-42a9dd9964f3"):
        return {"id": 14, "name": "Jets"}
    elif (api_team_id == "4809ecb0-abd3-451d-9c4a-92a90b83ca06"):
        return {"id": 15, "name": "Dolphins"}
    elif (api_team_id == "768c92aa-75ff-4a43-bcc0-f2798c2e1724"):
        return {"id": 16, "name": "Bills"}
    elif (api_team_id == "04aa1c9d-66da-489d-b16a-1dee3f2eec4d"):
        return {"id": 17, "name": "Giants"}
    elif (api_team_id == "e627eec7-bbae-4fa4-8e73-8e1d6bc5c060"):
        return {"id": 18, "name": "Cowboys"}
    elif (api_team_id == "22052ff7-c065-42ee-bc8f-c4691c50e624"):
        return {"id": 19, "name": "Football Team"}
    elif (api_team_id == "386bdbf9-9eea-4869-bb9a-274b0bc66e80"):
        return {"id": 20, "name": "Eagles"}
    elif (api_team_id == "f0e724b0-4cbf-495a-be47-013907608da9"):
        return {"id": 21, "name": "49ers"}
    elif (api_team_id == "2eff2a03-54d4-46ba-890e-2bc3925548f3"):
        return {"id": 22, "name": "Rams"}
    elif (api_team_id == "3d08af9e-c767-4f88-a7dc-b920c6d2b4a8"):
        return {"id": 23, "name": "Seahawks"}
    elif (api_team_id == "de760528-1dc0-416a-a978-b510d20692ff"):
        return {"id": 24, "name": "Cardinals"}
    elif (api_team_id == "33405046-04ee-4058-a950-d606f8c30852"):
        return {"id": 25, "name": "Vikings"}
    elif (api_team_id == "a20471b4-a8d9-40c7-95ad-90cc30e46932"):
        return {"id": 26, "name": "Packers"}
    elif (api_team_id == "7b112545-38e6-483c-a55c-96cf6ee49cb8"):
        return {"id": 27, "name": "Bears"}
    elif (api_team_id == "c5a59daa-53a7-4de0-851f-fb12be893e9e"):
        return {"id": 28, "name": "Lions"}
    elif (api_team_id == "4254d319-1bc7-4f81-b4ab-b5e6f3402b69"):
        return {"id": 29, "name": "Buccaneers"}
    elif (api_team_id == "e6aa13a4-0055-48a9-bc41-be28dc106929"):
        return {"id": 30, "name": "Falcons"}
    elif (api_team_id == "0d855753-ea21-4953-89f9-0e20aff9eb73"):
        return {"id": 31, "name": "Saints"}
    elif (api_team_id == "f14bf5cc-9a82-4a38-bc15-d39f75ed5314"):
        return {"id": 32, "name": "Panthers"}
    elif (api_team_id == "9dbb9060-ba0f-4920-829e-16d4d9246b5d"):
        return {"id": None, "name": "Chargers", "city": "San Diego"}
    else:
        return {"id": None, "name": None}

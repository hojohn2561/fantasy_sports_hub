# Fantasy Sports Hub
The one-stop shop for sports fans and fantasy sports fans alike. This website/SPA offers all the stats, highlights, and scores that a sports fan would want, but also more in-depth stats, trends, and analysis for fantasy sports players so that they can make the most well-informed decision to lift their team to victory. 

Stats are just numbers and it may be hard for one to analyze and interpret. This is what this website aims to solve.

## Table of Contents
1. [Features](#Features)
2. [Getting Started](#Getting-Started)
3. [Contributors](#Contributors)
4. [Acknowledgments](#Acknowledgments)

## Features
Planned, currently for NFL (other leagues will be implemented in similar structure):
- News (not yet implemented)
- Scores (not yet implemented)
- Stats (in development)
- Standings (in development)
- Schedules (in development)
- Power Rankings (not yet implemented)
- Fantasy Insider Stats (not yet implemented)
- DFS Lineup Optimizer (not yet implemented)

## Getting Started
This web app utilizes a [React](https://reactjs.org/) front-end and [Django-Rest](https://www.django-rest-framework.org/) back-end. This project also uses:
- A *nix environment,
- [Python 3.8.5](https://www.python.org/downloads/)
- [pip](https://github.com/pypa/pip)
- The [venv](https://docs.python.org/3/library/venv.html) Python module.
To get sports data, you need a SportRadar API key. Paste yours into the required location in configuration.py.
Currently, to run the application, use the command ```python manage.py runserver``` and then navigate to ```localhost:8000```.

## Contributors
- [John Ho](https://github.com/hojohn2561)

## Acknowledgments
- [Sportradar](https://sportradar.us/) for allowing use of its API for data.

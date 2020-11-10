import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import apiConfig from "../../apiConfig.json";

class NflDropdownMenu extends Component {
  state = {
    teamsByDivision: {},
  };

  sideMenuItems = [
    { label: "Home", to: "/nfl" },
    { label: "Scores", to: "/nfl/scores" },
    { label: "Stats", to: "/nfl/stats" },
    { label: "Standings", to: "/nfl/standings" },
    { label: "Schedule", to: "/nfl/schedule" },
    { label: "Teams", to: "/nfl/teams" },
    { label: "Power Rankings", to: "/nfl/power-rankings" },
    { label: "Fantasy Football", to: "/nfl/fantasy" },
    { label: "Fantasy Football Insider", to: "/nfl/fantasy-insider" },
    { label: "DFS Lineup Optimizer", to: "/nfl/dfs-lineup-optimizer" },
  ];

  componentDidMount() {
    axios.get(apiConfig.getNflTeamsEndpoint).then((response) => {
      const teamsData = response.data;
      const teamsByDivision = {};
      for (let i = 0; i < teamsData.length; i++) {
        const currentTeam = teamsData[i];
        const currentDivision = `${currentTeam.conference} ${currentTeam.division}`;
        if (!(currentDivision in teamsByDivision))
          teamsByDivision[currentDivision] = [currentTeam];
        else teamsByDivision[currentDivision].push(currentTeam);
      }

      this.setState({ teamsByDivision });
    });
  }

  render() {
    const { teamsByDivision } = this.state;

    return (
      <div className="container">
        <div className="col-2 navBarSideMenu ">
          {this.sideMenuItems.map((item) => (
            <div key={item.label} className="row ">
              <Link className="btn btn-light btn-block" to={item.to}>
                {item.label}
              </Link>
            </div>
          ))}
        </div>
        <div className="col">
          <div className="row">
            {Object.keys(teamsByDivision).map((key) =>
              key.includes("NFC") ? (
                <div className="col-3">
                  <h6>{key}</h6>
                  {teamsByDivision[key].map((team) => (
                    <div className="row">
                      <Link
                        className="btn btn-light btn-block"
                        to={`nfl/teams/${team.name}`}
                      >
                        <img
                          className="navBarTeamLogo"
                          src={team.logo}
                          alt={`${team.name}_logo`}
                        />
                        {team.name}
                      </Link>
                    </div>
                  ))}
                </div>
              ) : (
                ""
              )
            )}
          </div>
          <hr />
          <div className="row">
            {Object.keys(teamsByDivision).map((key) =>
              key.includes("AFC") ? (
                <div className="col-3">
                  <h6>{key}</h6>
                  {teamsByDivision[key].map((team) => (
                    <div className="row">
                      <Link
                        className="btn btn-light btn-block"
                        to={`nfl/teams/${team.name}`}
                      >
                        <img
                          className="navBarTeamLogo"
                          src={team.logo}
                          alt={`${team.name}_logo`}
                        />
                        {team.name}
                      </Link>
                    </div>
                  ))}
                </div>
              ) : (
                ""
              )
            )}
          </div>
        </div>
      </div>
    );
  }
}

export default NflDropdownMenu;

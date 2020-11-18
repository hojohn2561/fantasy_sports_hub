import React, { Component } from "react";
import BroadcastCellContent from "./BroadcastCellContent";
import WeatherCellContent from "./WeatherCellContent";

class GameInfoContent extends Component {
  getGameDayTime = (game_datetime) => {
    let gameDate = new Date(game_datetime);
    return gameDate.toLocaleTimeString("en-US", {
      hour: "numeric",
      minute: "numeric",
    });
  };

  render() {
    const { game, teamLogos } = this.props;
    const fullAwayTeamName = game["away_team_name"];
    const fullHomeTeamName = game["home_team_name"];

    switch (game["status"]) {
      case "closed":
        return (
          <div class="row" style={{ marginBottom: "15px" }}>
            <div class="col-8">
              {`${fullAwayTeamName} `}
              <img
                src={teamLogos[fullAwayTeamName]}
                className="scheduleTeamLogoIcon"
              />
              {` ${game["away_team_points"]} `} @
              {` ${game["home_team_points"]} `}
              <img
                src={teamLogos[fullHomeTeamName]}
                className="scheduleTeamLogoIcon"
              />{" "}
              {fullHomeTeamName}
            </div>
          </div>
        );
      case "postponed":
        return (
          <div class="row" style={{ marginBottom: "15px" }}>
            <div class="col-8">
              {`${fullAwayTeamName} `}{" "}
              <img
                src={teamLogos[fullAwayTeamName]}
                className="scheduleTeamLogoIcon"
              />{" "}
              @{" "}
              <img
                src={teamLogos[fullHomeTeamName]}
                className="scheduleTeamLogoIcon"
              />
              {` ${fullHomeTeamName} `}
            </div>
            <div class="col-4" style={{ alignContent: "end" }}>
              POSTPONED
            </div>
            <hr />
          </div>
        );
      case "scheduled":
        return (
          <div class="row" style={{ marginBottom: "15px" }}>
            <div class="col-8">
              {`${fullAwayTeamName} `}{" "}
              <img
                src={teamLogos[fullAwayTeamName]}
                className="scheduleTeamLogoIcon"
              />{" "}
              @{" "}
              <img
                src={teamLogos[fullHomeTeamName]}
                className="scheduleTeamLogoIcon"
              />
              {` ${fullHomeTeamName} `}
            </div>
            <div class="col-4" style={{ alignContent: "end" }}>
              {`${this.getGameDayTime(game["game_datetime"])} on `}
              <BroadcastCellContent
                broadcastNetwork={game["broadcast_network"]}
              />
            </div>

            <div class="w-100"></div>
            <div class="col">
              <WeatherCellContent
                weatherCondition={game["weather_conditions"]}
              />
            </div>
            <div class="col">{game["weather_wind"]}</div>
          </div>
        );
      default:
        return (
          <div class="row" style={{ marginBottom: "15px" }}>
            <div class="col-8">
              {`${fullAwayTeamName} @ ${fullHomeTeamName} `}
            </div>
            <div class="col-4" style={{ alignContent: "end" }}>
              {`${this.getGameDayTime(game["game_datetime"])} on `}
              <BroadcastCellContent
                broadcastNetwork={game["broadcast_network"]}
              />
            </div>

            <div class="w-100"></div>
            <div class="col">
              <WeatherCellContent
                weatherCondition={game["weather_conditions"]}
              />
            </div>
            <div class="col">{game["weather_wind"]}</div>
          </div>
        );
    }
  }
}

export default GameInfoContent;

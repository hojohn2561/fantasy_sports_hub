import React, { Component } from "react";
import BoxScoreTable from "./BoxScoreTable";
import BroadcastCellContent from "./BroadcastCellContent";
import WeatherCellContent from "./WeatherCellContent";
import RedCircle from "../../common/svgs/red_circle.svg";

class GameInfoContent extends Component {
  goToGamePage = () => {
    console.log("Go to game's page");
  };

  render() {
    const { game, teamLogos } = this.props;
    const {
      away_team_name: awayTeamFullName,
      home_team_name: homeTeamFullName,
      home_team_alias: homeTeamAlias,
      away_team_alias: awayTeamAlias,
    } = game;
    const awayTeamName = game["away_team_name"].split(" ")[
      game["away_team_name"].split(" ").length - 1
    ];
    const homeTeamName = game["home_team_name"].split(" ")[
      game["home_team_name"].split(" ").length - 1
    ];
    const awayTeamLogo = teamLogos[awayTeamFullName];
    const homeTeamLogo = teamLogos[homeTeamFullName];

    switch (game["status"]) {
      case "closed":
        const {
          away_team_points: awayTeamTotalPoints,
          away_team_quarter_1_points: awayTeamQ1Points,
          away_team_quarter_2_points: awayTeamQ2Points,
          away_team_quarter_3_points: awayTeamQ3Points,
          away_team_quarter_4_points: awayTeamQ4Points,
          home_team_points: homeTeamTotalPoints,
          home_team_quarter_1_points: homeTeamQ1Points,
          home_team_quarter_2_points: homeTeamQ2Points,
          home_team_quarter_3_points: homeTeamQ3Points,
          home_team_quarter_4_points: homeTeamQ4Points,
        } = game;
        const awayTeamPointsByQuarter = [
          awayTeamQ1Points,
          awayTeamQ2Points,
          awayTeamQ3Points,
          awayTeamQ4Points,
        ];
        const homeTeamPointsByQuarter = [
          homeTeamQ1Points,
          homeTeamQ2Points,
          homeTeamQ3Points,
          homeTeamQ4Points,
        ];

        return (
          <div
            className="card gameInfoCard"
            style={{ cursor: "pointer" }}
            onClick={this.goToGamePage}
          >
            <div className="card-body">
              <div className="row">
                <div className="col">
                  <div className="row justify-content-center">
                    <img src={awayTeamLogo} className="scheduleTeamLogoIcon" />
                    <span className="gameInfoCardText">{`${awayTeamAlias} ${awayTeamName}`}</span>
                  </div>
                  <div className="row justify-content-center">
                    <span className="scoreText">{`${awayTeamTotalPoints}`}</span>
                  </div>
                </div>
                <div className="col-auto">
                  <div className="row justify-content-center atSymbolText">
                    @
                  </div>
                  <div className="row justify-content-center scoreText">
                    FINAL
                  </div>
                </div>
                <div className="col">
                  <div className="row justify-content-center">
                    <img src={homeTeamLogo} className="scheduleTeamLogoIcon" />
                    <span className="gameInfoCardText">{`${homeTeamAlias} ${homeTeamName} `}</span>
                  </div>
                  <div className="row justify-content-center">
                    <span className="scoreText">{` ${homeTeamTotalPoints}`}</span>
                  </div>
                </div>
              </div>
              <div className="row pt-2">
                <div className="col-md-auto">
                  <BoxScoreTable
                    awayTeamAlias={awayTeamAlias}
                    awayTeamPointsByQuarter={awayTeamPointsByQuarter}
                    homeTeamAlias={homeTeamAlias}
                    homeTeamPointsByQuarter={homeTeamPointsByQuarter}
                  />
                </div>
                <div className="col">
                  <span className="medium">
                    <u>Team Leaders</u>
                  </span>
                </div>
              </div>
            </div>
          </div>
        );
      case "halftime":
      case "inprogress":
        // Make another API to get live stats. Schedule API doesn't get live points.
        return (
          <div className="card gameInfoCard">
            <div className="card-body h-100">
              <div className="row h-100">
                <div className="col">
                  <div className="row justify-content-center">
                    <img src={awayTeamLogo} className="scheduleTeamLogoIcon" />
                    <span className="gameInfoCardText">{`${awayTeamAlias} ${awayTeamName}`}</span>
                  </div>
                </div>
                <div className="col-auto">
                  <div className="row justify-content-center atSymbolText">
                    @
                  </div>
                  <div className="row justify-content-center scoreText">
                    <span>
                      <img src={RedCircle} className="recordIcon" /> Live
                    </span>
                  </div>
                </div>
                <div className="col">
                  <div className="row justify-content-center">
                    <img src={homeTeamLogo} className="scheduleTeamLogoIcon" />
                    <span className="gameInfoCardText">{`${homeTeamAlias} ${homeTeamName} `}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        );
      case "postponed":
        return (
          <div className="card gameInfoCard">
            <div className="card-body h-100">
              <div className="row h-100">
                <div className="col">
                  <div className="row justify-content-center">
                    <img src={awayTeamLogo} className="scheduleTeamLogoIcon" />
                    <span className="gameInfoCardText">{`${awayTeamAlias} ${awayTeamName}`}</span>
                  </div>
                </div>
                <div className="col-auto">
                  <div className="row justify-content-center atSymbolText">
                    @
                  </div>
                  <div className="row">
                    <p class="scoreText">POSTPONED</p>
                  </div>
                </div>
                <div className="col">
                  <div className="row justify-content-center">
                    <img src={homeTeamLogo} className="scheduleTeamLogoIcon" />
                    <span className="gameInfoCardText">{`${homeTeamAlias} ${homeTeamName} `}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        );
      case "created":
      case "scheduled":
        return (
          <div className="card gameInfoCard">
            <div className="card-body h-100">
              <div className="row h-100">
                <div className="col">
                  <div className="row justify-content-center">
                    <img src={awayTeamLogo} className="scheduleTeamLogoIcon" />
                    <span className="gameInfoCardText">{`${awayTeamAlias} ${awayTeamName}`}</span>
                  </div>
                  <div className="row justify-content-center">
                    <BroadcastCellContent
                      gameDateTime={game["game_datetime"]}
                      broadcastNetwork={game["broadcast_network"]}
                    />
                  </div>
                </div>
                <div className="col-auto">
                  <div className="row justify-content-center atSymbolText">
                    @
                  </div>
                </div>
                <div className="col">
                  <div className="row justify-content-center">
                    <img src={homeTeamLogo} className="scheduleTeamLogoIcon" />
                    <span className="gameInfoCardText">{`${homeTeamAlias} ${homeTeamName} `}</span>
                  </div>
                  <div className="row justify-content-center">
                    <WeatherCellContent
                      weatherCondition={game["weather_conditions"]}
                    />
                  </div>
                  <div className="row justify-content-center">
                    Wind: {game["weather_wind"]}
                  </div>
                </div>
              </div>
            </div>
          </div>
        );
      default:
        //console.log(`${awayTeamFullName} @ ${homeTeamFullName}... default`);
        return (
          <div className="row gameInfoRow">
            <div className="col-8">
              {`${awayTeamFullName} @ ${homeTeamFullName} `}
            </div>
            <div className="col-4" style={{ alignContent: "end" }}>
              <BroadcastCellContent
                gameDateTime={game["game_datetime"]}
                broadcastNetwork={game["broadcast_network"]}
              />
            </div>

            <div className="w-100"></div>
            <div className="col">
              <WeatherCellContent
                weatherCondition={game["weather_conditions"]}
              />
            </div>
            <div className="col">{game["weather_wind"]}</div>
          </div>
        );
    }
  }
}

export default GameInfoContent;

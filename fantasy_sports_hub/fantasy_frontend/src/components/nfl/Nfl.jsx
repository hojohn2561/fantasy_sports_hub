import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";
import ReactLoading from "react-loading";
import axios from "axios";
import apiConfig from "../../apiConfig.json";
import NflTicker from "./NflTicker";
import NflHome from "./NflHome";
import NflScores from "./scores/NflScores";
import NflStandings from "./standings/NflStandings";
import NflSchedule from "./schedule/NflSchedule";
import NflTeams from "./teams/NflTeams";
import NflTeamPage from "./teams/NflTeamPage";
import DfsLineupOptimizer from "./dfsLineupOptimizer/DfsLineupOptimizer";
import NflStats from "./stats/NflStats";

class Nfl extends Component {
  state = {
    teamsData: [],
    standingsYears: [2020, 2019, 2018, 2017, 2016, 2015],
    scheduleYears: [2020, 2019, 2018, 2017, 2016, 2015, 2014],
    standingsData: [],
    schedulesData: [],
    divisions: [],
    teamLogos: {},
    isLoading: true, // If loading, display the loading  animation
  };

  componentDidMount() {
    const { standingsYears, scheduleYears } = this.state;

    Promise.all([
      axios.get(apiConfig.getNflTeamsEndpoint),
      // ========================================================== THESE ARE GETTING STANDINGS DATA FOR EACH YEAR. REFACTOR THIS. ==========================================================
      axios.get(`${apiConfig.getNflStandingsEndpoint}${standingsYears[0]}`),
      axios.get(`${apiConfig.getNflStandingsEndpoint}${standingsYears[1]}`),
      axios.get(`${apiConfig.getNflStandingsEndpoint}${standingsYears[2]}`),
      axios.get(`${apiConfig.getNflStandingsEndpoint}${standingsYears[3]}`),
      axios.get(`${apiConfig.getNflStandingsEndpoint}${standingsYears[4]}`),
      axios.get(`${apiConfig.getNflStandingsEndpoint}${standingsYears[5]}`),
      axios.get(`${apiConfig.getNflSchedulesEndpoint}${scheduleYears[0]}`),
      axios.get(`${apiConfig.getNflSchedulesEndpoint}${scheduleYears[1]}`),
      axios.get(`${apiConfig.getNflSchedulesEndpoint}${scheduleYears[2]}`),
      axios.get(`${apiConfig.getNflSchedulesEndpoint}${scheduleYears[3]}`),
      axios.get(`${apiConfig.getNflSchedulesEndpoint}${scheduleYears[4]}`),
      axios.get(`${apiConfig.getNflSchedulesEndpoint}${scheduleYears[5]}`),
      axios.get(`${apiConfig.getNflSchedulesEndpoint}${scheduleYears[6]}`),
    ])
      .then(function (responses) {
        return Promise.all(
          responses.map(function (response) {
            return response;
          })
        );
      })
      .then((response) => {
        const teamsData = response[0].data;
        const standingsData = [
          // ============================================================================== AND REFACTOR THIS. ==============================================================================
          response[1].data,
          response[2].data,
          response[3].data,
          response[4].data,
          response[5].data,
          response[6].data,
        ];
        const schedulesData = [
          response[7].data,
          response[8].data,
          response[9].data,
          response[10].data,
          response[11].data,
          response[12].data,
          response[13].data,
        ];

        let divisions = [];
        let teamLogos = {};

        for (let i = 0; i < teamsData.length; i++) {
          let currentTeam = teamsData[i];
          let currentDivision = `${currentTeam.conference} ${currentTeam.division}`;
          if (!divisions.includes(currentDivision))
            divisions.push(currentDivision);

          let teamFullName = currentTeam["city"]
            .concat(" ")
            .concat(currentTeam["name"]);
          if (!teamLogos.hasOwnProperty(teamFullName))
            teamLogos[teamFullName] = currentTeam["logo"];
        }

        this.setState({
          teamsData,
          standingsData,
          schedulesData,
          divisions,
          teamLogos,
          isLoading: false,
        });
      });
  }

  render() {
    const {
      teamsData,
      teamLogos,
      divisions,
      standingsData,
      schedulesData,
      isLoading,
    } = this.state;

    // If still loading, display loading animation, otherwise, render the page
    if (isLoading) {
      return (
        <ReactLoading
          type="spin"
          color="#45DEFA"
          height={"20%"}
          width={"20%"}
        />
      );
    }

    return (
      <main>
        <NflTicker league="nfl" />
        <div className="container content">
          <Switch>
            <Route path="/nfl/scores" component={NflScores} />
            <Route
              path="/nfl/standings"
              render={(props) => (
                <NflStandings
                  teamsData={teamsData}
                  divisions={divisions}
                  standingsData={standingsData}
                  {...props}
                />
              )}
            />
            <Route
              path="/nfl/schedule"
              render={(props) => (
                <NflSchedule
                  teamsData={teamsData}
                  teamLogos={teamLogos}
                  schedulesData={schedulesData}
                  {...props}
                />
              )}
            />
            <Route
              path="/nfl/teams/:teamName"
              render={(props) => (
                <NflTeamPage teamsData={teamsData} {...props} />
              )}
            />
            <Route
              path="/nfl/teams"
              render={(props) => <NflTeams teamsData={teamsData} {...props} />}
            />
            <Route path="/nfl/stats" component={NflStats} />
            <Route
              path="/nfl/dfs-lineup-optimizer"
              component={DfsLineupOptimizer}
            />
            <Route path="/nfl" component={NflHome} />
          </Switch>
        </div>
      </main>
    );
  }
}

export default Nfl;

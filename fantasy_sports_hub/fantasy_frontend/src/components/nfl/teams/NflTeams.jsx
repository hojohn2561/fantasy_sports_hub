import React, { Component } from "react";
import NflTeamCard from "./NflTeamCard";
import "./teams.css";

class NflTeams extends Component {
  state = {};

  render() {
    const { teamsData } = this.props;

    // Goes inside the content div of the Nfl component
    return (
      <React.Fragment>
        {teamsData.map((team) => (
          <NflTeamCard key={team.name} team={team} />
        ))}
      </React.Fragment>
    );
  }
}

export default NflTeams;

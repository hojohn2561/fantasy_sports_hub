import React, { Component } from "react";
import NflTeamCard from "./NflTeamCard";
import "./teams.css";

class NflTeams extends Component {
  state = {};

  render() {
    const { teamsData } = this.props;

    // Goes inside the content div of the Nfl component
    return (
      <div>
        {teamsData.map((team) => (
          <NflTeamCard key={team.name} team={team} />
        ))}
      </div>
    );
  }
}

export default NflTeams;

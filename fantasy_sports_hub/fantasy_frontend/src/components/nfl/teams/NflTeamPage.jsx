import React, { Component } from "react";
import "./teams.css";

class NflTeamPage extends Component {
  state = {};

  render() {
    const { teamsData } = this.props;
    const { teamName: selectedTeamName } = this.props.match.params; // Get selected team name from URL

    const selectedTeam = teamsData.filter(
      (team) => selectedTeamName === team.name
    )[0]; // [0] because filter creates an array, and here we only have one element (the selected team's obj)

    console.log(selectedTeam);

    return (
      <React.Fragment>
        <div className="jumbotron jumbotron-fluid teamPageBanner">
          <h1 class="display-4">{selectedTeam.name}</h1>
        </div>
      </React.Fragment>
    );
  }
}

export default NflTeamPage;

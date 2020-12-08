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
          <div className="teamPageLogo float-left">
            <img
              className="teamPageLogoImage"
              src={selectedTeam.logo}
              alt={selectedTeam.name}
            />
          </div>
          <h1>
            {selectedTeam.city} {selectedTeam.name}
          </h1>
        </div>
      </React.Fragment>
    );
  }
}

export default NflTeamPage;

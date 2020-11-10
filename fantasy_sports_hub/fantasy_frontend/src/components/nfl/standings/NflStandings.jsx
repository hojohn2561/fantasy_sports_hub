import React, { Component } from "react";
import PropTypes from "prop-types";
import NflStandingsTable from "./NflStandingsTable";
import Select from "../../common/select/Select";
import _ from "lodash";
import "./standings.css";

class NflStandings extends Component {
  state = {
    sortColumn: { path: "win_percentage", order: "desc" },
    yearSelect: this.props.standingsData[0][0]["season_year"],
    seasonSelect: "Regular Season",
  };

  componentDidMount() {}

  handleSort = (sortColumn) => {
    this.setState({ sortColumn });
  };

  createYearSelect = () => {
    const { yearSelect } = this.state;
    const { standingsData } = this.props;

    // Create array of available options for the select menu
    const yearOptions = standingsData.map(
      (standingsDataObj) => standingsDataObj[0]["season_year"]
    );

    return (
      <Select
        id="yearSelect"
        name="yearSelect"
        value={yearSelect}
        handleChange={this.handleSelectChange}
        options={yearOptions}
      />
    );
  };

  createSeasonSelect = () => {
    const { seasonSelect } = this.state;
    let seasonOptions = ["Regular Season", "Pre Season"];

    return (
      <Select
        id="seasonSelect"
        name="seasonSelect"
        value={seasonSelect}
        handleChange={this.handleSelectChange}
        options={seasonOptions}
      />
    );
  };

  handleSelectChange = (event) => {
    // To dynamically update state with one handle function regardless of which select menu value was changed
    let elementName = event.target.name;
    let updatedValue = event.target.value;

    // If changed value is a number, convert the string to a number before updating state
    if (!isNaN(parseInt(updatedValue))) {
      this.setState({
        [elementName]: parseInt(updatedValue),
        sortColumn: { path: "win_percentage", order: "desc" }, // Reset to sort by win count
      });
    }
    // If changed value is not a number, just update state with the string
    else {
      this.setState({
        [elementName]: updatedValue,
        sortColumn: { path: "win_percentage", order: "desc" },
      });
    }
  };

  // Get standings data for the selected year only
  getStandingsForSelectedYear = () => {
    const { yearSelect } = this.state;
    const { teamsData, divisions, standingsData } = this.props;

    const standings = [];
    for (let i = 0; i < standingsData.length; i++) {
      let currentDataYear = standingsData[i][0].season_year;

      if (currentDataYear === parseInt(yearSelect)) {
        let standingsDataForSelectedYear = [...standingsData[i]];
        divisions.forEach((division) => {
          const teamsInDivision = teamsData.filter(
            (team) => division === `${team.conference} ${team.division}`
          );

          const standingsInDivision = standingsDataForSelectedYear.filter(
            (team) => division === `${team.division}` // Division in this obj is the full division name
          );

          // Use teamsInDivision to get team logo src and combine with standingsInDivision to create just one list
          standingsInDivision.forEach((curStandingTeam) => {
            teamsInDivision.forEach((curDivisionTeam) => {
              if (curDivisionTeam.name === curStandingTeam.name)
                curStandingTeam["logo"] = curDivisionTeam.logo;
            });
          });

          standings.push({ [division]: standingsInDivision }); // [] for dynamic key. ES6, won't work in IE and Edge 13
        });
        break;
      }
    }

    return standings;
  };

  render() {
    const { sortColumn, yearSelect } = this.state;
    console.log(this.state);

    // Filter out standings for selected year only
    let standings = this.getStandingsForSelectedYear();

    return (
      <div className="card border-dark mb-3 pageCard">
        <h1 className="pageHeader">NFL Standings - {yearSelect}</h1>
        <form className="form-inline standingsSelectForm">
          <div className="form-group mr-3">{this.createYearSelect()}</div>
          <div className="form-group">{this.createSeasonSelect()}</div>
        </form>

        {standings.map((divisionStandings) => {
          const sorted = _.orderBy(
            divisionStandings[Object.keys(divisionStandings)[0]],
            // Sort by the path, if the same, sort by win_percentage. More-wining teams first.
            [sortColumn.path, "win_percentage"],
            [sortColumn.order, sortColumn.order === "desc" ? "asc" : "desc"]
          );

          return (
            <NflStandingsTable
              division={Object.keys(divisionStandings)[0]}
              currentDivisionStandings={sorted}
              sortColumn={sortColumn}
              onSort={this.handleSort}
            />
          );
        })}
      </div>
    );
  }
}

NflStandings.propTypes = {
  teamsData: PropTypes.array,
  divisions: PropTypes.array,
  standingsData: PropTypes.array,
};

export default NflStandings;

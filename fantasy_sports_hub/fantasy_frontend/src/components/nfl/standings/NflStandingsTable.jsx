import React, { Component } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import Table from "../../common/table/Table";

class NflStandingsTable extends Component {
  columns = [
    { label: "W", description: "Wins", path: "win_count" },
    { label: "L", description: "Losses", path: "loss_count" },
    { label: "T", description: "Ties", path: "tie_count" },
    { label: "PCT", description: "Winning Percentage", path: "win_percentage" },
    {
      label: "HOME",
      description: "Home Record",
      // multiPaths is used for displaying a concatenation of multiple properties, separated by the delimiter
      multiPaths: ["home_win_count", "home_loss_count", "home_tie_count"],
      delimeter: "-",
    },
    {
      label: "ROAD",
      description: "Loss Record",
      multiPaths: ["road_win_count", "road_loss_count", "road_tie_count"],
      delimeter: "-",
    },
    {
      label: "DIV",
      description: "Division Record",
      multiPaths: [
        "division_win_count",
        "division_loss_count",
        "division_tie_count",
      ],
      delimeter: "-",
    },
    {
      label: "CONF",
      description: "Conference Record",
      multiPaths: [
        "conference_win_count",
        "conference_loss_count",
        "conference_tie_count",
      ],
      delimeter: "-",
    },
    {
      label: "NON-CONF",
      description: "Non Conference Record",
      multiPaths: [
        "non_conference_win_count",
        "non_conference_loss_count",
        "non_conference_tie_count",
      ],
      delimeter: "-",
    },
    { label: "PF", description: "Points For", path: "points_for" },
    { label: "PA", description: "Points Against", path: "points_against" },
    {
      label: "DIFF",
      description: "Points Differential",
      path: "points_differential",
    },
    {
      label: "STRK",
      description: "Streak",
      multiPaths: ["streak_type", "streak_length"],
      delimeter: "",
    },
  ];

  render() {
    const {
      division,
      currentDivisionStandings,
      sortColumn,
      onSort,
    } = this.props;

    // Format data before passing to Table component so Table just renders the content of the table
    const data = [];
    currentDivisionStandings.forEach((teamStanding) => {
      const rowContent = {
        rowHeaderCell: (
          <Link
            className="card-link" // Want card-link styling here (no underline on mouse hover)
            to={`teams/${teamStanding.name}/stats`}
          >
            <img src={teamStanding.logo} className="standingsTableIcon" />{" "}
            <span className="standingsTableTeamName">
              {`${teamStanding.city} ${teamStanding.name}`}
            </span>
          </Link>
        ),
        rowData: teamStanding,
      };
      data.push(rowContent);
    });

    return (
      <Table
        title={division}
        columns={this.columns}
        data={data}
        classNames="table table-bordered table-striped rounded-top standingsTable"
        sortColumn={sortColumn}
        onSort={onSort}
        rowHeaderSyles={{ width: "22%", textAlign: "left" }}
      />
    );
  }
}

NflStandingsTable.propTypes = {
  divsion: PropTypes.string,
  currentDivisionStandings: PropTypes.array,
  sortColumn: PropTypes.object,
  onSort: PropTypes.func,
};

export default NflStandingsTable;

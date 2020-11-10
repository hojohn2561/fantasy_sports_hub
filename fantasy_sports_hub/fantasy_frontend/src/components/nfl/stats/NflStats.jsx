import React, { Component } from "react";
import NflStatsTable from "./NflStatsTable";
import "./stats.css";

class NflStats extends Component {
  offenseGroupName = "offense";
  defenseGroupName = "defense";
  kickGroupName = "kick";
  teamGroupName = "team";

  statLabels = [
    { label: "Offensive Leaders", group: this.offenseGroupName },
    { label: "Defensive Leaders", group: this.defenseGroupName },
    { label: "Kicking Leaders", group: this.kickGroupName },
    { label: "Team Rankings", group: this.teamGroupName },
  ];

  statCategories = [
    { category: "Passing Yards", group: this.offenseGroupName },
    { category: "Passing Touchdowns", group: this.offenseGroupName },
    { category: "Rushing Yards", group: this.offenseGroupName },
    { category: "Rushing Touchdowns", group: this.offenseGroupName },
    { category: "Receiving Yards", group: this.offenseGroupName },
    { category: "Receiving Touchdowns", group: this.offenseGroupName },
    { category: "Tackles", group: this.defenseGroupName },
    { category: "Interceptions", group: this.defenseGroupName },
    { category: "Fumbles", group: this.defenseGroupName },
    { category: "Sacks", group: this.defenseGroupName },
    { category: "Field Goals Made", group: this.kickGroupName },
    { category: "Longest Field Goal Made", group: this.kickGroupName },
    { category: "Passing Yards/Game", group: this.teamGroupName },
    { category: "Rushing Yards/Game", group: this.teamGroupName },
    { category: "Yards/Game Allowed", group: this.teamGroupName },
    { category: "Touchdowns Allowed", group: this.teamGroupName },
    { category: "Forced Turnovers", group: this.teamGroupName },
    { category: "Defensive Touchdowns", group: this.teamGroupName },
  ];

  state = {
    offensiveStats: [],
    defensiveStats: [],
    sortColumn: { path: "passing_yds", order: "desc" },
  };

  componentDidMount() {
    const { offensiveStats, defensiveStats } = this.state;
    this.setState({ offensiveStats, defensiveStats });
  }

  handleSort = (sortColumn) => {
    this.setState({ sortColumn });
  };

  render() {
    const { sortColumn } = this.state;

    return (
      <div>
        {/* For offense, defense, and team stats */}
        {this.statLabels.map((statLabel) => (
          <div id={`${statLabel}StatCharts`}>
            <h1>{statLabel.label}</h1>
            {/* Create the stat table under the corresponding label/category (offense, defense, or team) */}
            {this.statCategories.map((statCategory) =>
              statLabel.group === statCategory.group ? (
                <div className="card statsCard">
                  <NflStatsTable
                    category={statCategory.category}
                    sortColumn={sortColumn}
                    onSort={this.handleSort}
                  />
                </div>
              ) : null
            )}
          </div>
        ))}
      </div>
    );
  }
}

export default NflStats;

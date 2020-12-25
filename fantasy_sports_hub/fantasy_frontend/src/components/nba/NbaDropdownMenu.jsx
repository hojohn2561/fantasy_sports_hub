import React, { Component } from "react";
import { Link } from "react-router-dom";

class NbaDropdownMenu extends Component {
  state = {};

  sideMenuItems = [
    { label: "Home", to: "/" },
    // { label: "Scores", to: "/" },
    // { label: "Stats", to: "/" },
    // { label: "Standings", to: "/" },
    // { label: "Schedule", to: "/" },
    // { label: "Teams", to: "/" },
    // { label: "Power Rankings", to: "/" },
    // { label: "Fantasy Football", to: "/" },
    // { label: "Fantasy Football Insider", to: "/" },
    { label: "DFS Lineup Optimizer", to: "/nba/dfs-lineup-optimizer" },
  ];

  render() {
    return (
      <div className="container">
        <div className="col-2 navBarSideMenu ">
          {this.sideMenuItems.map((item) => (
            <div key={item.label} className="row ">
              <Link className="btn btn-light btn-block" to={item.to}>
                {item.label}
              </Link>
            </div>
          ))}
        </div>
        <div className="col"></div>
      </div>
    );
  }
}

export default NbaDropdownMenu;

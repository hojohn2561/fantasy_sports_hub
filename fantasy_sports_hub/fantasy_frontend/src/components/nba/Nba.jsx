import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";
import NbaHome from "./NbaHome";
import NbaDfsLineupOptimizer from "./dfsLineupOptimizer/NbaDfsLineupOptimizer";

class Nba extends Component {
  state = {};
  render() {
    return (
      <main>
        <div className="container content">
          <Switch>
            <Route
              path="/nba/dfs-lineup-optimizer"
              component={NbaDfsLineupOptimizer}
            />
            <Route path="/nba" component={NbaHome} />
          </Switch>
        </div>
      </main>
    );
  }
}

export default Nba;

import React from "react";
import { Route, Redirect, Switch } from "react-router-dom";
import NavBar from "./components/common/navbar/NavBar";
import Home from "./components/home/Home";
import Nfl from "./components/nfl/Nfl";
import Nba from "./components/nba/Nba";
import "./App.css";

function App() {
  return (
    <div className="shadeWhite">
      <NavBar />
      <main className="container">
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Redirect exact from="/home" to="/" />
          {/* If current path is /nfl, render the Nfl component. That component renders the pages content depending 
            on the rest of the path. In other words, all of the nfl pages shares the Nfl component (the parent) */}
          <Route path="/nfl" component={Nfl}></Route>
          <Route path="/nba" component={Nba}></Route>
        </Switch>
      </main>
    </div>
  );
}

export default App;

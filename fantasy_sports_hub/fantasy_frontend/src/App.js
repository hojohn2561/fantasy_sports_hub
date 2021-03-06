import React from "react";
import { Route, Redirect, Switch } from "react-router-dom";
import NavBar from "./components/common/navbar/NavBar";
import Home from "./components/home/Home";
import Nfl from "./components/nfl/Nfl";
import Nba from "./components/nba/Nba";
import Nhl from "./components/nhl/Nhl";
import Mlb from "./components/mlb/Mlb";
import Ufc from "./components/ufc/Ufc";
import NotFound from "./components/not_found/NotFound";
import Footer from "./components/common/footer/Footer";
import "./App.css";

function App() {
  return (
    <div className="shadeWhite">
      <NavBar />
      <Switch>
        <Route exact path="/" component={Home}></Route>
        <Redirect exact from="/home" to="/" />
        {/* If current path is /nfl, render the Nfl component. That component renders the pages content depending 
          on the rest of the path. In other words, all of the nfl pages shares the Nfl component (the parent) */}
        <Route path="/nfl" component={Nfl}></Route>
        <Route path="/nba" component={Nba}></Route>
        <Route path="/nhl" component={Nhl}></Route>
        <Route path="/mlb" component={Mlb}></Route>
        <Route path="/ufc" component={Ufc}></Route>
        {/* Not working because Django pages, instead of React components, are served when URLs are entered manually.
        Root cause seems to be the same as not initially starting on the / page on first use */}
        {/* <Route component={NotFound}></Route> */}
      </Switch>
      <Footer />
    </div>
  );
}

export default App;

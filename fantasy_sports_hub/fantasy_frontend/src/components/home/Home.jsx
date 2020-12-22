import React, { Component } from "react";
import HeadlineCardImage from "../common/images/jalen-hurts.png";
import HeadlinesCard from "../common/card/HeadlinesCard";

class Home extends Component {
  headlineLinks = [
    {
      headline: "NFL playoff clinching scenarios for Week 13",
      to: "/nfl",
    },
    {
      headline: "What should the Eagles do with Wentz?",
      to: "/nfl",
    },
    {
      headline: "NBA 2020-2021 season to begin on 12/22",
      to: "/nba",
    },
  ];

  headlineSlides = [
    {
      title: "Quarterback Controversy Looming?",
      description:
        "With the Eagles' division title aspirations diminishing, is it time to take a closer look at what Jalen Hurts can do?",
      imageLink: "",
    },
  ];

  state = {};

  render() {
    return (
      <div className="content container">
        <h1>Main Home Page</h1>
        <div className="row">
          <div className="col-8">
            <div className="card">
              <img
                className="card-img-top headline-card-image"
                src={HeadlineCardImage}
                alt="Headline Card Image"
              />
              <div className="card-body">
                <h5 className="card-title">Quarterback Controversy Looming?</h5>
                <p className="card-text">
                  With the Eagles' division title aspirations diminishing, is it
                  time to take a closer look at what Jalen Hurts can do?
                </p>
              </div>
            </div>
          </div>
          <div className="col-4">
            <HeadlinesCard
              title={"Top Headlines"}
              headlines={this.headlineLinks}
            ></HeadlinesCard>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;

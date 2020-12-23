import React, { Component } from "react";
import HeadlinesCard from "../common/card/HeadlinesCard";
import HeadlinesCarousel from "../common/card/HeadlinesCarousel";
import HeadlineCardImage1 from "../common/images/steelers-vs-football_team.jpg";
import HeadlineCardImage2 from "../common/images/jalen-hurts.png";
import HeadlineCardImage3 from "../common/images/nba-stars.jpg";

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
      title: "Washington Football Team at Pittsburgh Steelers",
      description:
        "Can the Steelers keep their undefeated season alive as the Washington Football Team comes to visit?",
      image: HeadlineCardImage1,
    },
    {
      title: "Quarterback Controversy Looming?",
      description:
        "With the Eagles' division title aspirations diminishing, is it time to take a closer look at what Jalen Hurts can do?",
      image: HeadlineCardImage2,
    },
    {
      title: "The NBA is Back!",
      description: "The NBA Season is set to begin on 12/22.",
      image: HeadlineCardImage3,
    },
  ];

  state = {};

  render() {
    return (
      <div className="content container">
        <h1>Main Home Page</h1>
        <div className="row">
          <div className="col-8">
            <HeadlinesCarousel
              headlineSlides={this.headlineSlides}
            ></HeadlinesCarousel>
          </div>
          <div className="col-4">
            <HeadlinesCard
              title={"Top Headlines"}
              headlineLinks={this.headlineLinks}
            ></HeadlinesCard>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;

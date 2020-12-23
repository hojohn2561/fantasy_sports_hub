import React, { Component } from "react";
import HeadlinesCard from "../common/card/HeadlinesCard";
import HeadlinesCarousel from "../common/card/HeadlinesCarousel";
import HeadlineCardImage1 from "../common/images/steelers-vs-football_team.jpg";
import HeadlineCardImage2 from "../common/images/jalen-hurts.png";

class NflHome extends Component {
  state = {};

  headlineLinks = [
    {
      headline: "Playoff clinching scenarios for Week 13",
      to: "/nfl",
    },
    {
      headline: "Updated draft order: Top five unchanged",
      to: "/nfl",
    },
    {
      headline: "Power Rankings: Steelers remain at #1",
      to: "/nfl",
    },
    {
      headline: "What should the Eagles do with Wentz?",
      to: "/nfl",
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
  ];

  render() {
    return (
      <div>
        <div class="row">
          <div class="col-8">
            <HeadlinesCarousel
              headlineSlides={this.headlineSlides}
            ></HeadlinesCarousel>
          </div>
          <div class="col-4">
            <HeadlinesCard
              title={"Headlines"}
              headlineLinks={this.headlineLinks}
            ></HeadlinesCard>
          </div>
        </div>
      </div>
    );
  }
}

export default NflHome;

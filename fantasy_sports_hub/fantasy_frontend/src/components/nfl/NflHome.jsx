import React, { Component } from "react";
import HeadlinesCard from "../common/card/HeadlinesCard";
import HeadlineCardImage from "../common/images/jalen-hurts.png";

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

  render() {
    return (
      <div>
        <div class="row">
          <div class="col-8">
            <div class="card">
              <img
                class="card-img-top headline-card-image"
                src={HeadlineCardImage}
                alt="Headline Card Image"
              />
              <div class="card-body">
                <h5 class="card-title">Quarterback Controversy Looming?</h5>
                <p class="card-text">
                  With the Eagles' division title aspirations diminishing, is it
                  time to take a closer look at what Jalen Hurts can do?
                </p>
              </div>
            </div>
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

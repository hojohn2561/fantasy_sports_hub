import React, { Component } from "react";
import HeadlineCardImage from "../common/images/jalen-hurts.png";

class NflHome extends Component {
  state = {};
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
          <div class="col-4">col-4</div>
        </div>
      </div>
    );
  }
}

export default NflHome;

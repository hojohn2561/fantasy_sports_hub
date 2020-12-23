import React from "react";
import { Link } from "react-router-dom";

const HeadlinesCard = ({ title, headlineLinks }) => {
  return (
    <div className="card headlines-panel-card">
      <div className="card-header">{title}</div>
      <div class="card-body">
        {headlineLinks.map((headline) => (
          <div>
            <Link to={headline.to}>{headline.headline}</Link>
            <hr />
          </div>
        ))}
      </div>
    </div>
  );
};

export default HeadlinesCard;

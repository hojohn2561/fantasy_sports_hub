import React from "react";
import PropTypes from "prop-types";

const BroadcastCellContent = ({ broadcastNetwork }) => {
  let svgSource = "";
  let broadcastClassName = "";

  switch (broadcastNetwork) {
    case "NBC":
      svgSource =
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/NBC_logo.svg";
      broadcastClassName = "nbcChannelIcon";
      break;
    case "CBS":
      svgSource =
        "https://upload.wikimedia.org/wikipedia/commons/4/4e/CBS_logo.svg";
      broadcastClassName = "cbsChannelIcon";
      break;
    case "FOX":
      svgSource =
        "https://upload.wikimedia.org/wikipedia/commons/e/ea/NFL_on_Fox_2014.svg";
      broadcastClassName = "foxChannelIcon";
      break;
    case "ESPN":
      svgSource =
        "https://upload.wikimedia.org/wikipedia/commons/2/2f/ESPN_wordmark.svg";
      broadcastClassName = "espnChannelIcon";
      break;
    default:
      return <span>{broadcastNetwork}</span>;
  }

  return (
    <span>
      <img src={svgSource} className={broadcastClassName} />
    </span>
  );
};

BroadcastCellContent.propTypes = {
  broadcastChannel: PropTypes.string,
};

export default BroadcastCellContent;

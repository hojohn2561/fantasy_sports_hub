import React from "react";
import rightArrow from "./valid_right_arrow.png";

const RightArrow = ({ handleClick }) => {
  return (
    <img
      src={rightArrow}
      className="rightTickerArrow"
      style={{ cursor: "pointer" }}
      onClick={handleClick}
    />
  );
};

export default RightArrow;

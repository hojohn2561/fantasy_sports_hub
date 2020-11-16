import React from "react";
import rightArrow from "./valid_right_arrow.png";

const RightArrow = ({ handleClick }) => {
  return (
    <img src={rightArrow} className="rightTickerArrow" onClick={handleClick} />
  );
};

export default RightArrow;

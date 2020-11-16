import React from "react";
import leftArrow from "./valid_left_arrow.png";

const LeftArrow = ({ handleClick }) => {
  return (
    <img src={leftArrow} className="leftTickerArrow" onClick={handleClick} />
  );
};

export default LeftArrow;

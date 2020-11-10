import React from "react";

const RightArrow = ({ onClick, ...rest }) => {
  // onMove means if dragging or swiping in progress.
  return <i class="fas fa-arrow-right" onClick={onClick} />;
};

export default RightArrow;

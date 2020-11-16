import React from "react";
import invalidLeftArrow from "./invalid_left_arrow.png";
import invalidRightArrow from "./invalid_right_arrow.png";
import leftArrow from "./valid_left_arrow.png";
import rightArrow from "./valid_right_arrow.png";

const CustomButtonGroupAsArrows = ({ next, previous, ...rest }) => {
  console.log(rest);
  const { carouselState } = rest; // rest contains the carousel state

  return (
    <React.Fragment>
      <div onClick={previous}>
        {carouselState.currentSlide === 0 ? (
          <img src={invalidLeftArrow} className="leftTickerArrow" /> // Display greyed out arrow when can't go back
        ) : (
          <img src={leftArrow} className="leftTickerArrow" />
        )}
      </div>
      <div onClick={next}>
        {
          // Display greyed out arrow when can't go forward
          // carouselState.totalItems = Total number of slides.
          // carouselState.slidesToShow = Number of slides to show at a time
          // Difference between the two properties is the number of possible moves to right
          carouselState.currentSlide ===
          carouselState.totalItems - carouselState.slidesToShow ? (
            <img src={invalidRightArrow} className="rightTickerArrow" />
          ) : (
            <img src={rightArrow} className="rightTickerArrow" />
          )
        }
      </div>
    </React.Fragment>
  );
};

export default CustomButtonGroupAsArrows;

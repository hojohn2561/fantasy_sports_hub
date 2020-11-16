import React from "react";
import ValidLeftArrow from "./ValidLeftArrow";
import ValidRightArrow from "./ValidRightArrow";
import InvalidRightArrow from "./InvalidRightArrow";
import InvalidLeftArrow from "./InvalidLeftArrow";

const CustomButtonGroupAsArrows = ({ next, previous, ...rest }) => {
  //console.log(rest);
  const { carouselState } = rest; // rest contains the carousel state

  return (
    <React.Fragment>
      <div onClick={previous}>
        {carouselState.currentSlide === 0 ? (
          <InvalidLeftArrow /> // Display greyed out arrow when can't go back
        ) : (
          <ValidLeftArrow handleClick={previous} />
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
            <InvalidRightArrow />
          ) : (
            <ValidRightArrow handleClick={next} />
          )
        }
      </div>
    </React.Fragment>
  );
};

export default CustomButtonGroupAsArrows;

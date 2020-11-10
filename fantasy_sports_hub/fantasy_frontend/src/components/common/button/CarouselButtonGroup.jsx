import React from "react";

const CarouselButtonGroup = ({ next, previous, ...rest }) => {
  const {
    carouselState: { currentSlide, totalItems, slidesToShow },
  } = rest;

  return (
    <div className="carousel-button-group">
      <button
        aria-label="Go to previous slide"
        style={
          currentSlide === 0
            ? { display: "none" }
            : { margin: "-60px -0px 0px 220px" }
        }
        // If true and truthy, return the last operand
        className={
          currentSlide !== 0 &&
          "react-multiple-carousel__arrow react-multiple-carousel__arrow--left"
        }
        onClick={() => previous()}
      ></button>
      <button
        aria-label="Go to next slide"
        style={
          currentSlide === totalItems - slidesToShow
            ? { display: "none" }
            : { margin: "-60px 220px 0px 0px" }
        }
        className={
          currentSlide !== totalItems - slidesToShow &&
          "react-multiple-carousel__arrow react-multiple-carousel__arrow--right"
        }
        onClick={() => next()}
      ></button>
    </div>
  );
};

export default CarouselButtonGroup;

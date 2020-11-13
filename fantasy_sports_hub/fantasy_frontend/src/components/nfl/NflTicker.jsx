import React, { Component } from "react";
import Carousel from "react-multi-carousel";
import CarouselButtonGroup from "../common/button/CarouselButtonGroup";

class NflTicker extends Component {
  responsive = {
    superLargeDesktop: {
      breakpoint: { max: 4000, min: 3000 },
      items: 10,
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 8,
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2,
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 2,
    },
  };

  render() {
    return (
      <Carousel
        responsive={this.responsive}
        arrows={false}
        renderButtonGroupOutside={true}
        customButtonGroup={
          <CarouselButtonGroup
            next={this.props.next}
            previous={this.props.previous}
            rest={this.props.rest}
          />
        }
      >
        <div className="scoresCarouselItem shadeGray">Item 1</div>
        <div className="scoresCarouselItem shadeGray">Item 2</div>
        <div className="scoresCarouselItem shadeGray">Item 3</div>
        <div className="scoresCarouselItem shadeGray">Item 4</div>
        <div className="scoresCarouselItem shadeGray">Item 5</div>
        <div className="scoresCarouselItem shadeGray">Item 6</div>
        <div className="scoresCarouselItem shadeGray">Item 7</div>
        <div className="scoresCarouselItem shadeGray">Item 8</div>
        <div className="scoresCarouselItem shadeGray">Item 9</div>
        <div className="scoresCarouselItem shadeGray">Item 10</div>
        <div className="scoresCarouselItem shadeGray">Item 11</div>
        <div className="scoresCarouselItem shadeGray">Item 12</div>
      </Carousel>
    );
  }
}

export default NflTicker;

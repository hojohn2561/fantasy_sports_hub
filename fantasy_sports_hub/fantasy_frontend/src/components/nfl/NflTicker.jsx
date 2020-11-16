import React, { Component } from "react";
import Carousel from "react-multi-carousel";
import CustomButtonGroupAsArrows from "../common/carousel/CustomButtonGroupAsArrows";
import "./carousel.css";

class NflTicker extends Component {
  state = {
    items: [
      "Item 1",
      "Item 2",
      "Item 3",
      "Item 4",
      "Item 5",
      "Item 6",
      "Item 7",
      "Item 8",
      "Item 9",
      "Item 10",
      "Item 11",
      "Item 12",
      "Item 13",
      "Item 14",
      "Item 15",
      "Item 16",
      "Item 17",
      "Item 18",
    ],
  };

  responsive = {
    superLargeDesktop: {
      breakpoint: { max: 4000, min: 3000 },
      items: 12,
      slidesToSlide: 1,
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 10,
      slidesToSlide: 1,
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 5,
      slidesToSlide: 1,
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 3,
      slidesToSlide: 1,
    },
  };

  handleClick = () => {
    console.log("arrow clicked");
  };

  render() {
    const { items } = this.state;
    console.log(this.state);

    return (
      <div className="carousel">
        <Carousel
          responsive={this.responsive}
          arrows={false} // Hide/Show the default arrows
          draggable={true}
          className="ticker"
          renderButtonGroupOutside={true}
          customButtonGroup={<CustomButtonGroupAsArrows />}
        >
          {items.map((item) => (
            <div className="scoresCarouselItem shadeGray">{item}</div>
          ))}
        </Carousel>
      </div>
    );
  }
}

export default NflTicker;

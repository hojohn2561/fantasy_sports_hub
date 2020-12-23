import React, { Component } from "react";
import Carousel from "react-multi-carousel";

class HeadlinesCarousel extends Component {
  responsive = {
    superLargeDesktop: {
      breakpoint: { max: 4000, min: 3000 },
      items: 1,
      slidesToSlide: 1,
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 1,
      slidesToSlide: 1,
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 1,
      slidesToSlide: 1,
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1,
      slidesToSlide: 1,
    },
  };

  render() {
    const { headlineSlides } = this.props;

    return (
      <Carousel
        responsive={this.responsive}
        showDots={true}
        draggable={false}
        autoPlaySpeed={2000}
      >
        {headlineSlides.map((headline) => (
          <div className="card">
            <img
              class="card-img-top headline-card-image"
              src={headline.image}
              alt="Headline Card Image"
            />
            <div class="card-body headline-card-body">
              <h5 class="card-title">{headline.title}</h5>
              <p class="card-text">{headline.description}</p>
            </div>
          </div>
        ))}
      </Carousel>
    );
  }
}

export default HeadlinesCarousel;

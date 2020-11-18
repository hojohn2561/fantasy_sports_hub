import React from "react";
import PropTypes from "prop-types";
import SunnyDIcon from "./images/wi-day-sunny.svg";
import CloudyWindyDIcon from "./images/wi-day-cloudy-windy.svg";
import CloudyDIcon from "./images/wi-day-cloudy.svg";
import RainyDIcon from "./images/wi-day-rain.svg";
import CloudyIcon from "./images/wi-cloudy.svg";

const WeatherCellContent = ({ weatherCondition }) => {
  switch (weatherCondition) {
    case "Clear":
    case "Clear Skies":
    case "Clear, Sunny":
    case "Sunny":
    case "Mostly Sunny":
      return (
        <span>
          <img src={SunnyDIcon} className="weatherIcon" /> {weatherCondition}
        </span>
      );
    case "Partly Cloudy":
      return (
        <span>
          <img src={CloudyDIcon} className="weatherIcon" /> {weatherCondition}
        </span>
      );
    case "Cloudy":
    case "Mostly Cloudy":
      return (
        <span>
          <img src={CloudyIcon} className="weatherIcon" /> {weatherCondition}
        </span>
      );
    case "Mostly Cloudy":
      return <span>{weatherCondition}</span>;
    case "Rain":
      return (
        <span>
          <img src={RainyDIcon} className="weatherIcon" /> {weatherCondition}
        </span>
      );
    case "N/A (Indoors)":
      return <span>{weatherCondition}</span>;
    case "Controlled Climate":
      return <span>{weatherCondition}</span>;
    case "Cloudy and Windy":
      return (
        <span>
          <img src={CloudyWindyDIcon} className="weatherIcon" />{" "}
          {weatherCondition}
        </span>
      );
    case "Light Snow/Fog":
      return <span>{weatherCondition}</span>;
    default:
      return <span>{weatherCondition}</span>;
  }
};

WeatherCellContent.propTypes = {
  weatherCondition: PropTypes.string,
};

export default WeatherCellContent;

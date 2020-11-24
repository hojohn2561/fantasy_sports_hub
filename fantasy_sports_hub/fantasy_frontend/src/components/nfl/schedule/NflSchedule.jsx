import React, { Component } from "react";
import Select from "../../common/select/Select";
import GameInfoContent from "./GameInfoContent";
import "./schedule.css";

class NflSchedule extends Component {
  state = {
    yearSelect: this.props.schedulesData[0][0]["season_year"],
    weekSelectOptions: Array.from({ length: 17 }, (_, i) => "Week " + (i + 1)), // Array with numbers 1 to 17
    weekSelect: "Week 11",
  };

  daysInWeek = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  monthsInYear = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  nflGameDaysInWeekOrder = [
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
  ];
  componentDidMount() {}

  createYearSelect = () => {
    const { yearSelect } = this.state;
    const { schedulesData } = this.props;

    // Create array of available options for the select menu
    const yearOptions = schedulesData.map(
      (schedulesDataObj) => schedulesDataObj[0]["season_year"]
    );

    return (
      <Select
        id="yearSelect"
        name="yearSelect"
        value={yearSelect}
        handleChange={this.handleSelectChange}
        options={yearOptions}
      />
    );
  };

  handleSelectChange = (event) => {
    let elementName = event.target.name;
    let updatedValue = event.target.value;

    // If changed value is a number, convert the string to a number before updating state
    if (!isNaN(parseInt(updatedValue)))
      this.setState({ [elementName]: parseInt(updatedValue) });
    // If changed value is not a number, just update state with the string
    else this.setState({ [elementName]: updatedValue });
  };

  getScheduleForSelectedWeekInYear = () => {
    const { yearSelect, weekSelect } = this.state;
    const { schedulesData } = this.props;

    // Organize games by date in the week
    const schedule = {};

    for (let i = 0; i < schedulesData.length; i++) {
      let currentDataYear = schedulesData[i][0].season_year;

      if (currentDataYear === parseInt(yearSelect)) {
        let scheduleDataForSelectedYear = [...schedulesData[i]];
        console.log(scheduleDataForSelectedYear);

        const gamesInSelectedWeek = scheduleDataForSelectedYear.filter(
          (game) => game["week_num"] === parseInt(weekSelect.split(" ")[1]) // weekSelect.split(" ")[1] is the week number selected
        );

        //console.log(gamesInSelectedWeek);
        //console.log(new Date(gamesInSelectedWeek[0]["game_datetime"]));

        gamesInSelectedWeek.forEach((game) => {
          let gameDate = new Date(game["game_datetime"]);
          let gameDateFormatted = `${this.daysInWeek[gameDate.getDay()]}, ${
            this.monthsInYear[gameDate.getMonth()]
          } ${gameDate.getDate()}`;
          console.log(gameDateFormatted);

          // If new game date, add it to the json. Otherwise, append it to the list of games on that date
          if (!(gameDateFormatted in schedule)) {
            schedule[gameDateFormatted] = [game];
            //console.log(schedule);
          } else {
            schedule[gameDateFormatted].push(game);
          }
        });

        break;
      }
    }

    return schedule;
  };

  sortWeekScheduleByDay = (gamesInWeek) => {
    let sortedGamesInWeek = [];

    for (let i = 0; i < this.nflGameDaysInWeekOrder.length; i++) {
      let day = this.nflGameDaysInWeekOrder[i];
      for (let key of Object.keys(gamesInWeek)) {
        if (key.split(",")[0] === day) {
          sortedGamesInWeek.push(gamesInWeek[key]);
        }
      }
    }

    // Sort games in day by time (1 PM, 4 PM, 8 PM)
    sortedGamesInWeek.forEach((gameDay) =>
      gameDay.sort((game1, game2) =>
        game1["game_datetime"] > game2["game_datetime"]
          ? 1
          : game1["game_datetime"] < game2["game_datetime"]
          ? -1
          : 0
      )
    );
    return sortedGamesInWeek;
  };

  getGameDayCardHeader = (game_datetime) => {
    let gameDate = new Date(game_datetime);

    return (
      <h4>
        {`${this.daysInWeek[gameDate.getDay()]}, ${
          this.monthsInYear[gameDate.getMonth()]
        } ${gameDate.getDate()}`}
      </h4>
    );
  };

  render() {
    const { yearSelect, weekSelect, weekSelectOptions } = this.state;
    const { teamLogos } = this.props;
    //console.log(this.state);
    console.log(this.props);

    // Filter out standings for selected year only
    let gamesInWeek = this.getScheduleForSelectedWeekInYear();
    let sortedGamesInWeek = this.sortWeekScheduleByDay(gamesInWeek);
    console.log(sortedGamesInWeek);

    return (
      <div className="card border-dark mb-3 pageCard">
        <h1 className="pageHeader">NFL Schedule - {yearSelect}</h1>
        <form className="form-inline standingsSelectForm">
          <div className="form-group mr-3">{this.createYearSelect()}</div>
          <div className="form-group mr-3">
            <Select
              id="weekSelect"
              name="weekSelect"
              value={weekSelect}
              handleChange={this.handleSelectChange}
              options={weekSelectOptions}
            />
          </div>
        </form>

        {sortedGamesInWeek.map((gameDay) => (
          <div className="card gameDayCard">
            <div class="card-header">
              {this.getGameDayCardHeader(gameDay[0]["game_datetime"])}
            </div>
            <div className="card-body">
              {gameDay.map((game) => (
                <GameInfoContent game={game} teamLogos={teamLogos} />
              ))}
            </div>
          </div>
        ))}
      </div>
    );
  }
}

export default NflSchedule;

import React, { Component } from "react";
import Select from "../../common/select/Select";

class NflSchedule extends Component {
  state = {
    yearSelect: this.props.schedulesData[0][0]["season_year"],
    weekSelectOptions: Array.from({ length: 17 }, (_, i) => "Week " + (i + 1)), // Array with numbers 1 to 17
    weekSelect: "Week 9",
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

  createWeekSelect = () => {
    const { weekSelect, weekSelectOptions } = this.state;

    return (
      <Select
        id="weekSelect"
        name="weekSelect"
        value={weekSelect} // Initially selected option
        handleChange={this.handleSelectChange}
        options={weekSelectOptions}
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

        console.log(gamesInSelectedWeek);
        console.log(new Date(gamesInSelectedWeek[0]["game_datetime"]));

        gamesInSelectedWeek.forEach((game) => {
          let gameDate = new Date(game["game_datetime"]);
          let gameDateFormatted = `${this.daysInWeek[gameDate.getDay()]}, ${
            this.monthsInYear[gameDate.getMonth()]
          } ${gameDate.getDate()}`;
          console.log(gameDateFormatted);

          // If new game date, add it to the json. Otherwise, append it to the list of games on that date
          if (!(gameDateFormatted in schedule)) {
            schedule[gameDateFormatted] = [game];
            console.log(schedule);
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

  getGameDayTime = (game_datetime) => {
    let gameDate = new Date(game_datetime);
    return gameDate.toLocaleTimeString("en-US", {
      hour: "numeric",
      minute: "numeric",
    });
  };

  render() {
    const { yearSelect } = this.state;

    console.log(this.state);
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
          <div className="form-group mr-3">{this.createWeekSelect()}</div>
        </form>

        {sortedGamesInWeek.map((gameDay) => (
          <div className="card">
            <div class="card-header">
              {this.getGameDayCardHeader(gameDay[0]["game_datetime"])}
            </div>
            <div className="card-body">
              {gameDay.map((game) => (
                <p class="card-text">
                  {`${game["away_team_name"]} @ ${
                    game["home_team_name"]
                  } ${this.getGameDayTime(game["game_datetime"])}`}
                </p>
              ))}
            </div>
          </div>
        ))}
      </div>
    );
  }
}

export default NflSchedule;

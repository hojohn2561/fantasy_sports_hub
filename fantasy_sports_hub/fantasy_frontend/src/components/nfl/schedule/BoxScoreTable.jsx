import React from "react";

const BoxScoreTable = ({
  awayTeamAlias,
  awayTeamPointsByQuarter,
  homeTeamAlias,
  homeTeamPointsByQuarter,
}) => {
  return (
    <table class="table table-sm table-bordered mb-5">
      <thead>
        <tr>
          <th scope="col">Q</th>
          <th scope="col">1</th>
          <th scope="col">2</th>
          <th scope="col">3</th>
          <th scope="col">4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">{awayTeamAlias}</th>
          {awayTeamPointsByQuarter.map((awayTeamPointsInQuarter) => (
            <td>{awayTeamPointsInQuarter}</td>
          ))}
        </tr>
        <tr>
          <th scope="row">{homeTeamAlias}</th>
          {homeTeamPointsByQuarter.map((homeTeamPointsInQuarter) => (
            <td>{homeTeamPointsInQuarter}</td>
          ))}
        </tr>
      </tbody>
    </table>
  );
};

export default BoxScoreTable;

import React from "react";
import { Link } from "react-router-dom";

const NflTeamCardBody = ({ team }) => {
  let teamName = team.name;

  return (
    <div className="card-body">
      <Link className="card-link" to={`teams/${teamName}`}>
        Team Page
      </Link>
      <Link className="card-link" to={`teams/${teamName}/roster`}>
        Roster
      </Link>
      <Link className="card-link" to={`teams/${teamName}/schedule`}>
        Schedule
      </Link>
      <Link className="card-link" to={`teams/${teamName}/stats`}>
        Stats
      </Link>
    </div>
  );
};

export default NflTeamCardBody;

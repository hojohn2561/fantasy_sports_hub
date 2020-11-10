import React from "react";

const NflTeamCardHeader = ({ team }) => {
  const backgroundImage = {
    backgroundImage: "url(" + team.logo + ")",
    backgroundColor: team.primary_color,
    backgroundBlendMode: "normal",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "110%",
    backgroundSize: "50%",
  };

  return (
    <div className="card-header teamCardHeader" style={backgroundImage}>
      <div className="teamCardLogo float-left">
        <img className="teamCardLogoImage" src={team.logo} alt={team.name} />
      </div>
      <h5 className="card-title teamCardTitle">{team.city}</h5>
      <h2 className="card-title teamCardTitle">{team.name}</h2>
    </div>
  );
};

export default NflTeamCardHeader;

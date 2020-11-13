import React from "react";
import NflTeamCardHeader from "./NflTeamCardHeader";
import NflTeamCardBody from "./NflTeamCardBody";

const NflTeamCard = ({ team }) => {
  return (
    <div className="card rounded-top teamCard shadeWhite">
      <NflTeamCardHeader team={team} />
      <NflTeamCardBody team={team} />
    </div>
  );
};

export default NflTeamCard;

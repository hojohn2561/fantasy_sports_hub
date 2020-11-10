import React from "react";
import { Link } from "react-router-dom";

const NavBarLogo = ({ to, logo }) => {
  return (
    <Link className="navbar-brand" to={to}>
      {logo}
    </Link>
  );
};

export default NavBarLogo;

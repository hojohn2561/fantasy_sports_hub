import React from "react";
import { NavLink } from "react-router-dom";
import PropTypes from "prop-types";
import NavBarDropdown from "./NavBarDropdown";

const NavBarSection = ({ navBarItem, openDropdown, closeDropdown }) => {
  return (
    <li
      className="nav-item dropdown"
      onMouseEnter={() => openDropdown(navBarItem.label)}
    >
      <NavLink className="nav-link" to={navBarItem.to}>
        {navBarItem.label}
      </NavLink>
      <NavBarDropdown navBarItem={navBarItem} closeDropdown={closeDropdown} />
    </li>
  );
};

NavBarSection.propTypes = {
  navBarItems: PropTypes.array,
  openDropdown: PropTypes.func,
  closeDropdown: PropTypes.func,
};

export default NavBarSection;

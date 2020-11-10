import React from "react";
import PropTypes from "prop-types";
import NavBarSection from "./NavBarSection";

const NavBarBody = ({ navBarItems, openDropdown, closeDropdown }) => {
  return (
    <div className="collapse navbar-collapse" id="navbarNav">
      <ul className="navbar-nav">
        {navBarItems.map((navBarItem) => (
          <NavBarSection
            key={navBarItem.label}
            navBarItem={navBarItem}
            openDropdown={openDropdown}
            closeDropdown={closeDropdown}
          ></NavBarSection>
        ))}
      </ul>
    </div>
  );
};

NavBarBody.propTypes = {
  navBarItems: PropTypes.array,
  openDropdown: PropTypes.func,
  closeDropdown: PropTypes.func,
};

export default NavBarBody;

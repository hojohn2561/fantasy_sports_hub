import React from "react";

const NavBarDropdown = ({ navBarItem, closeDropdown }) => {
  return (
    <div
      style={
        navBarItem.isDropdownOpen ? { display: "block" } : { display: "none" }
      }
      className="dropdown-menu navbarDropdownMenu"
      onMouseLeave={() => closeDropdown(navBarItem.label)}
    >
      {navBarItem.dropdownMenu}
    </div>
  );
};

export default NavBarDropdown;

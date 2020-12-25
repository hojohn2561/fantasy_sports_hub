import React, { Component } from "react";
import NavBarLogo from "./NavBarLogo";
import NavBarBody from "./NavBarBody";
import NflDropdownMenu from "../../nfl/NflDropdownMenu";
import NbaDropdownMenu from "../../nba/NbaDropdownMenu";
import "./navBar.css";

// To add another NavBar element, add the object to this.state.navBarItems
class NavBar extends Component {
  state = {
    navBarItems: [
      {
        label: "NFL",
        to: "/nfl",
        isDropdownOpen: false,
        dropdownMenu: <NflDropdownMenu />,
      },
      {
        label: "NBA",
        to: "/nba",
        isDropdownOpen: false,
        dropdownMenu: <NbaDropdownMenu />,
      },
      { label: "NHL", to: "/nba", isDropdownOpen: false },
      { label: "NHL", to: "/nhl", isDropdownOpen: false },
      { label: "MLB", to: "/mlb", isDropdownOpen: false },
      { label: "MMA", to: "/mma", isDropdownOpen: false },
    ],
  };

  // Open dropdown when mouse enters the option's <li>. When opening a dropdown,
  // all other dropdowns should close.
  openDropdown = (label) => {
    const navBarItems = [...this.state.navBarItems];
    // Close all dropdowns
    navBarItems.forEach((item) => (item.isDropdownOpen = false));
    // Get the option's dropdown to open object and set isDropdownOpen to true
    const hoveredItem = navBarItems.find((item) => item.label === label);
    const index = navBarItems.indexOf(hoveredItem);
    hoveredItem.isDropdownOpen = true;
    // Replace the the object with isDropdownOpen=false with one now true
    navBarItems[index] = hoveredItem;
    // Update the state
    this.setState({ navBarItems });
  };

  // Close dropdown when mouse leaves the dropdown
  closeDropdown = (label) => {
    const navBarItems = [...this.state.navBarItems];
    const hoveredItem = navBarItems.find((item) => item.label === label);
    const index = navBarItems.indexOf(hoveredItem);
    hoveredItem.isDropdownOpen = false;
    navBarItems[index] = hoveredItem;

    this.setState({ navBarItems });
  };

  render() {
    const { navBarItems } = this.state;
    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <NavBarLogo to="/" logo="Fantasy-Sports" />
        <NavBarBody
          navBarItems={navBarItems}
          openDropdown={this.openDropdown}
          closeDropdown={this.closeDropdown}
        />
      </nav>
    );
  }
}

export default NavBar;

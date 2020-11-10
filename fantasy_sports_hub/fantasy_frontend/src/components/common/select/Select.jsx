import React from "react";
import PropTypes from "prop-types";

const Select = ({ id, name, value, handleChange, options }) => {
  console.log(value);

  return (
    <select
      className="form-control form-control-sm"
      id={id}
      name={name}
      value={value}
      onChange={handleChange}
    >
      {options.map((option) => (
        <option value={option}>{option}</option>
      ))}
    </select>
  );
};

Select.propTypes = {
  id: PropTypes.string,
  name: PropTypes.string,
  value: PropTypes.number || PropTypes.string, // Index of the selected option
  handleChange: PropTypes.func,
  options: PropTypes.array,
};

export default Select;

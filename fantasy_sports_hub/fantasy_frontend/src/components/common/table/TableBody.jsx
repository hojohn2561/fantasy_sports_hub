import React, { Component } from "react";
import PropTypes from "prop-types";
import _ from "lodash";

class TableBody extends Component {
  renderCell = (item, column) => {
    // Cell contains the property of the column. Get it.
    if (column.path) return _.get(item, column.path);
    // Cell contains multiple properties for the column
    else if (column.multiPaths) {
      // Pick the needed properties
      const properties = _.pick(item, column.multiPaths);
      // Get just the values (don't need the keys)
      const propertyValues = [];
      for (var key in properties) {
        propertyValues.push(properties[key]);
      }
      // Join the with the delimter and return to be displayed in the table cell
      return propertyValues.join(column.delimeter);
    }
    return "-------";
  };

  render() {
    const { data, columns } = this.props;

    return (
      <tbody>
        {data.map((item) => (
          <tr>
            <th scope="row" style={{ textAlign: "left" }}>
              {item.rowHeaderCell}
            </th>
            {columns.map((column) => (
              <td>{this.renderCell(item.rowData, column)}</td>
            ))}
          </tr>
        ))}
      </tbody>
    );
  }
}

TableBody.propTypes = {
  data: PropTypes.array,
  columns: PropTypes.array,
};

export default TableBody;

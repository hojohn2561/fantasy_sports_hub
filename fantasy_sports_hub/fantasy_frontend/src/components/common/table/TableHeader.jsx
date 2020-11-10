import React, { Component } from "react";
import PropTypes from "prop-types";

class TableHeader extends Component {
  raiseSort = (path) => {
    const { onSort } = this.props;
    const sortColumn = { ...this.props.sortColumn };

    if (sortColumn.path === path)
      sortColumn.order = sortColumn.order === "desc" ? "asc" : "desc";
    else {
      sortColumn.path = path;
      sortColumn.order = "desc";
    }

    onSort(sortColumn);
  };

  renderSortIcon = (column) => {
    const { sortColumn } = this.props;

    if (column.path !== sortColumn.path) return null;
    if (sortColumn.order === "desc") return <i className="fa fa-sort-desc" />;
    return <i className="fa fa-sort-asc" />;
  };

  render() {
    const { title, columns, rowHeaderSyles } = this.props;

    return (
      <thead>
        <tr>
          <th scope="col" style={rowHeaderSyles}>
            <h5 className="standingsTableHeader">{title}</h5>
          </th>
          {columns.map((column) => (
            <th
              scope="col"
              // Sort only when column has a single path property
              onClick={column.path ? () => this.raiseSort(column.path) : ""}
            >
              {column.label} {this.renderSortIcon(column)}
            </th>
          ))}
        </tr>
      </thead>
    );
  }
}

TableHeader.propTypes = {
  title: PropTypes.array,
  columns: PropTypes.array,
  sortColumn: PropTypes.object,
  onSort: PropTypes.func,
  rowHeaderSyles: PropTypes.object,
};

export default TableHeader;

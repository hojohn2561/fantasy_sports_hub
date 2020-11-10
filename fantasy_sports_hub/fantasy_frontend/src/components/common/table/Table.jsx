import React from "react";
import PropTypes from "prop-types";
import TableHeader from "./TableHeader";
import TableBody from "./TableBody";

const Table = ({
  columns,
  title,
  data,
  classNames,
  sortColumn,
  onSort,
  tableStyles,
  rowHeaderSyles,
}) => {
  //console.log(columns);
  //console.log(data);
  return (
    <table className={classNames} style={tableStyles}>
      <TableHeader
        title={title}
        columns={columns}
        sortColumn={sortColumn}
        onSort={onSort}
        rowHeaderSyles={rowHeaderSyles}
      />
      <TableBody data={data} columns={columns} />
    </table>
  );
};

Table.propTypes = {
  title: PropTypes.array,
  columns: PropTypes.array,
  data: PropTypes.array,
  classNames: PropTypes.string,
  sortColumn: PropTypes.object,
  onSort: PropTypes.func,
  rowHeaderSyles: PropTypes.object,
};

export default Table;

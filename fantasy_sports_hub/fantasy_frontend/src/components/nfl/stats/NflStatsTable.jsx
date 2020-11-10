import React, { Component } from "react";
import Table from "../../common/table/Table";

class NflStatsTable extends Component {
  passCompletionColumns = [
    { label: "Yards", description: "Yards", path: "passing_yds" },
  ];
  render() {
    const { category, sortColumn, onSort } = this.props;

    // Format data before passing to Table component so Table just renders the content of the table
    const data = [];

    return (
      <Table
        title={category}
        columns={this.passCompletionColumns}
        data={[
          { name: "Dak Prescott", passing_yds: "1690" },
          { name: "Tom Brady", passing_yds: "1375" },
          { name: "Josh Allen", passing_yds: "1326" },
          { name: "Russell Wilson", passing_yds: "1285" },
          { name: "Matt Ryan", passing_yds: "1246" },
        ]}
        classNames="table table-borderless"
        sortColumn={sortColumn}
        onSort={onSort}
        rowHeaderSyles={{ width: "75%", textAlign: "left" }}
      />
    );
  }
}

export default NflStatsTable;

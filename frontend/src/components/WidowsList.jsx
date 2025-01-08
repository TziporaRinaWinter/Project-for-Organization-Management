import * as React from "react";
import { DataGrid } from "@mui/x-data-grid";
import Paper from "@mui/material/Paper";

const columns = [
  { field: "id", headerName: "מ.ז.", width: 70 },
  { field: "firstName", headerName: "שם פרטי", width: 130 },
  { field: "lastName", headerName: "שם משפחה", width: 130, sortable: true },
  { field: "age", headerName: "גיל", width: 90, type: "number" },
  // {
  //   field: 'fullName',
  //   headerName: 'Full name',
  //   sortable: true,
  //   width: 160,
  //   valueGetter: (value, row) => `${row.firstName || ''} ${row.lastName || ''}`,
  // },
];

const rows = [
  { id: 1, lastName: "לוי", firstName: "פלוני", age: 35 },
  { id: 2, lastName: "כהן", firstName: "אלמוני", age: 42 },
  { id: 3, lastName: "לוי", firstName: "בבהלהח", age: 45 },
  { id: 4, lastName: "כעיחל", firstName: "כאכה", age: 16 },
  { id: 5, lastName: "טטגטד", firstName: "כאעטט", age: null },
  { id: 6, lastName: "עיחל", firstName: null, age: 150 },
  { id: 7, lastName: "סאטה", firstName: "טכללחה", age: 44 },
  { id: 8, lastName: "ראטו", firstName: "גחבב", age: 36 },
  { id: 9, lastName: "ףםך", firstName: "טאוט", age: 65 },
];

export default function DataTable() {
  return (
    <>
      <h2>אלמנות:</h2>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          width: "60%",
          margin: "0 auto",
        }}
      >
        <DataGrid
          rows={rows}
          columns={columns}
          checkboxSelection
          sx={{
            border: 0,
            "& .MuiDataGrid-cell": {
              justifyContent: "flex-start",
              textAlign: "right",
            },
            ".css-1gak8h1-MuiToolbar-root-MuiTablePagination-toolbar": {
              display: "none",
            },
          }}
        />
      </div>
    </>
  );
}

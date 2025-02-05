import React, { useState, useEffect } from "react";
import { DataGrid, useGridApiRef } from "@mui/x-data-grid";
import WidowService from "../../services/WidowService";
import { Button, Paper } from "@mui/material";
import BorderColorIcon from "@mui/icons-material/BorderColor";

const columns = [
  {
    field: "identity_number",
    headerName: "מ.ז.",
    width: 140,
    // valueGetter: (params) => params.row.identity_number || "",
  },
  {
    field: "first_name",
    headerName: "שם",
    width: 120,
    sortable: true,
    // valueGetter: (params) => params.row.first_name || "",
  },
  {
    field: "last_name",
    headerName: "משפחה",
    width: 120,
    sortable: true,
    // valueGetter: (params) => params.row.last_name || "",
  },
  {
    field: "mobile_phone",
    headerName: "נייד",
    width: 140,
    // valueGetter: (params) => params.row.phone || "",
  },
  {
    field: "action",
    headerName: "",
    width: 90,
    renderCell: (params) => (
      <Button onClick={() => handleButtonClick(params.row.id)}>
        <BorderColorIcon color="success" />
      </Button>
    ),
  },
];

const WidowsList = () => {
  const [widows, setWidows] = useState([]);
  const [error, setError] = useState(null);
  const widowService = new WidowService();
  const apiRef = useGridApiRef();

  useEffect(() => {
    const loadWidows = async () => {
      try {
        const data = await widowService.getWidows();
        console.log(data);
        setWidows(data);
      } catch (err) {
        setError(err.message);
      }
    };
    loadWidows();
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  const paginationModel = {
    page: 0,
    pageSize: 3,
    textAlign: "right",
    footerRowSelected: "שורות נבחרות: {0}",
  };

  return (
    <>
      <h2>אמהות:</h2>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          width: "80%",
          margin: "0 auto",
        }}
      >
        <DataGrid
          rows={widows}
          columns={columns}
          initialState={{ pagination: { paginationModel } }}
          pageSizeOptions={[3, 10, 50]}
          checkboxSelection
          getRowId={(row) => row.id}
          localeText={{
            footerRowSelected: (count) => `שורות נבחרות: ${count}`,
            footerTotalRows: () => "סך הכל שורות:",
            footerPaginationLabel: (from, to, count) =>
              `עמוד ${from} מתוך ${to}`,
            footerPaginationRowsPerPage: () => "שורות בעמוד:",
          }}
          sx={{
            border: 0,
            "& .MuiDataGrid-cell": {
              justifyContent: "flex-start",
              textAlign: "right",
            },
            ".css-1gak8h1-MuiToolbar-root-MuiTablePagination-toolbar": {
              direction: "ltr",
              justifySelf: "center",
            },
          }}
        />
      </div>
    </>
  );
};

export default WidowsList;

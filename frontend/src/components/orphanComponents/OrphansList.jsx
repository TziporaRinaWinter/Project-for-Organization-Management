import React, { useState, useEffect } from "react";
import { DataGrid, useGridApiRef } from "@mui/x-data-grid";
import OrphanService from "../../services/OrphanService";
import { Button, Paper } from "@mui/material";
import BorderColorIcon from "@mui/icons-material/BorderColor";
import { useNavigate } from "react-router-dom";

const columns = [
  {
    field: "identity_number",
    headerName: "מ.ז.",
    width: 140,
  },
  {
    field: "first_name",
    headerName: "שם",
    width: 120,
    sortable: true,
  },
  {
    field: "last_name",
    headerName: "משפחה",
    width: 120,
    sortable: true,
  },
  {
    field: "action",
    headerName: "",
    width: 90,
    renderCell: (params) => (
      <Button onClick={() => params.onSelectOrphan(params.row.id)}>
        <BorderColorIcon color="success" />
      </Button>
    ),
  },
];

const OrphanList = () => {
  const [orphans, setOrphans] = useState([]);
  const [error, setError] = useState(null);
  const orphanService = new OrphanService();
  const navigate = useNavigate();

  useEffect(() => {
    const loadOrphan = async () => {
      try {
        const data = await orphanService.getOrphans();
        console.log(data);
        setOrphans(data);
      } catch (err) {
        setError(err.message);
      }
    };
    loadOrphan();
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  const handleSelectOrphan = (id) => {
    navigate(`/child/${id}`);
  };

  const paginationModel = {
    page: 0,
    pageSize: 5,
  };

  return (
    <>
      <h2>ילדים:</h2>
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
          rows={orphans}
          columns={columns.map((col) => ({
            ...col,
            renderCell:
              col.field === "action"
                ? (params) => (
                    <Button onClick={() => handleSelectOrphan(params.row.id)}>
                      <BorderColorIcon color="success" />
                    </Button>
                  )
                : col.renderCell,
          }))}
          initialState={{ pagination: { paginationModel } }}
          pageSizeOptions={[5, 10, 50]}
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

export default OrphanList;

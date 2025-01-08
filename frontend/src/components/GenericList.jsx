import React from "react";
import { Card, CardContent, Typography } from "@mui/material";
import { makeStyles } from "@mui/styles";

const useStyles = makeStyles({
  card: {
    margin: "1vw",
  },
  headerContent: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
});

const GenericList = ({ title, data }) => {
  const classes = useStyles();

  const renderCard = (item) => (
    <Card key={item.id} variant="outlined" className={classes.card}>
      <CardContent className={classes.headerContent}>
        <Typography variant="h6">{item.name}</Typography>
        <Typography variant="h6">{item.detail}</Typography>
      </CardContent>
    </Card>
  );

  return (
    <div style={{}}>
      <h3>{title}</h3>
      {data.map(renderCard)}
    </div>
  );
};

export default GenericList;

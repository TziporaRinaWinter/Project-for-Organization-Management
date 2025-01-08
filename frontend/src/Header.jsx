import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import { Link } from "react-router-dom";

function Header({ pages }) {
  return (
    <AppBar
      position="sticky"
      sx={{ backgroundColor: "rgba(111, 174, 111, 0.82)" }}
    >
      <Container>
        <Toolbar>
          <Box
            sx={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              width: "95%",
            }}
          >
            {/* logo===== sx={{ display: { xs: "none", md: "flex" }, mr: 1 }} /> */}
            <Typography
              variant="h3"
              noWrap
              component="a"
              href="/home"
              sx={{
                mr: 2,
                display: "flex",
                fontWeight: 700,
                letterSpacing: ".3rem",
                color: "inherit",
                textDecoration: "none",
              }}
            >
              אחותי - ארגון אלמנות ויתומים
            </Typography>
            <Box
              sx={{
                flexGrow: 1,
                display: "flex",
              }}
            >
              {pages.map((page) => (
                <Link
                  key={page.href}
                  to={page.href}
                  style={{ textDecoration: "none", color: "inherit" }}
                >
                  <Button
                    variant="outlined"
                    sx={{
                      my: 2,
                      color: "ButtonText",
                      display: "block",
                      backgroundColor: "white",
                      border: "solid rgb(0, 81, 0) 1px",
                      boxShadow: "none",
                      margin: "5px",
                    }}
                  >
                    {page.title}
                  </Button>
                </Link>
              ))}
            </Box>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}
export default Header;

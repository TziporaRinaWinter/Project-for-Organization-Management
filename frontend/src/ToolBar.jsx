import * as React from "react";
import { extendTheme, styled } from "@mui/material/styles";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import { Link, Route, Routes } from "react-router-dom";
import { AppProvider } from "@toolpad/core/AppProvider";
import { DashboardLayout } from "@toolpad/core/DashboardLayout";
import { PageContainer } from "@toolpad/core/PageContainer";

const demoTheme = extendTheme({
  colorSchemes: { light: true, dark: true },
  colorSchemeSelector: "class",
});

function useDemoRouter(initialPath) {
  const [pathname, setPathname] = React.useState(initialPath);

  const router = React.useMemo(() => {
    return {
      pathname,
      searchParams: new URLSearchParams(),
      navigate: (path) => setPathname(String(path)),
    };
  }, [pathname]);

  return router;
}

// קומפוננטות דוגמה
const Dashboard = () => <div>Dashboard Content</div>;
const Orders = () => <div>Orders Content</div>;
const Reports = () => <div>Reports Content</div>;

export default function DashboardLayoutBasic(props) {
  const { pages } = props;
  const router = useDemoRouter("/home");

  return (
    <AppProvider navigation={pages} router={router} theme={demoTheme}>
      <PageContainer>
        <DashboardLayout>
          <Routes>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/orders" element={<Orders />} />
            <Route path="/reports" element={<Reports />} />
          </Routes>
        </DashboardLayout>
      </PageContainer>
    </AppProvider>
  );
}

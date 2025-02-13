import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import AppWidow from "./components/widowComponents/AppWidow";
import EventsList from "./components/eventComponents/EventsList";
import Home from "./components/homeComponents/Home";
import Header from "./Header";
import AppOrphan from "./components/orphanComponents/AppOrphan";

const pages = [
  { title: "בית", href: "/home", element: <Home /> },
  { title: "אמהות", href: "/mathers", element: <AppWidow /> },
  { title: "ילדים", href: "/children", element: <AppOrphan /> },
  { title: "ניהול ארועים", href: "/eventManagement", element: <EventsList /> },
];

function App() {
  return (
    <BrowserRouter>
      <Header pages={pages} />
      <Routes>
        {pages.map((page) => (
          <Route key={page.title} path={page.href} element={page.element} />
        ))}
        <Route path="/" element={<Home />} />
        <Route path="/mather/:id" element={<AppWidow />} />
        <Route path="/child/:id" element={<AppOrphan />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

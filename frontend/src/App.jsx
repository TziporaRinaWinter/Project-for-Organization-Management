import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import WidowsList from "./components/widowComponents/WidowsList";
import OrphansList from "./components/orphanComponents/OrphansList";
import EventsList from "./components/eventComponents/EventsList";
import Home from "./components/homeComponents/Home";
import Header from "./Header";

const pages = [
  { title: "בית", href: "/home", element: <Home /> },
  { title: "אלמנות", href: "/widowsList", element: <WidowsList /> },
  { title: "יתומים", href: "/orphansList", element: <OrphansList /> },
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
      </Routes>
    </BrowserRouter>
  );
}

export default App;

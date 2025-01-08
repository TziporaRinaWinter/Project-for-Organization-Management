import React from "react";
import GenericList from "./GenericList";

const EventsList = () => {
  const data = [
    { id: 1, name: "אלמנט 1", detail: "פרט 1" },
    { id: 2, name: "אלמנט 2", detail: "פרט 2" },
    { id: 3, name: "אלמנט 1", detail: "פרט 1" },
    { id: 4, name: "אלמנט 2", detail: "פרט 2" },
    { id: 5, name: "אלמנט 1", detail: "פרט 1" },
    { id: 6, name: "אלמנט 2", detail: "פרט 2" },
    { id: 7, name: "אלמנט 1", detail: "פרט 1" },
    { id: 8, name: "אלמנט 2", detail: "פרט 2" },
    { id: 9, name: "אלמנט 1", detail: "פרט 1" },
  ];

  return <GenericList title="ניהול אירועים:" data={data} />;
};

export default EventsList;

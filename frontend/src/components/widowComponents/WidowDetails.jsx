import React, { useEffect, useState } from "react";
import WidowService from "../../services/WidowService";

const WidowDetails = ({ widowId }) => {
  const [widow, setWidow] = useState(null);
  const widowService = new WidowService();

  useEffect(() => {
    const loadWidow = async () => {
      try {
        const data = await widowService.getWidowById(widowId);
        console.log(data[0]);
        setWidow(data[0]);
      } catch (err) {
        setError(err.message);
      }
    };
    loadWidow();
  }, [widowId]);

  if (!widow) return <div>טוען...</div>;

  return (
    <div>
      <h2>פרטי אלמנה</h2>
      {/* כאן תוכל להוסיף טופס לעריכה */}
      <p>{widowId}</p>
      <p>מ.ז: {widow.identity_number}</p>
      <p>שם: {widow.first_name}</p>
      <p>משפחה: {widow.last_name}</p>
      {/* טופס לעריכה */}
      address_id : 5 bank_account_id : 5 birth_date : "2020-02-01" email :
      "0505@gmail.com" first_name : "פלונית" hebrew_birth_date : null home_phone
      : "050512345" id : 4 identity_number : "123456789" last_name : "אלמונית"
      mobile_phone : "0505123456" num_of_minor_children : 5
      num_of_unmarried_children : 10 widowhood_date : "2022-04-01"
    </div>
  );
};

export default WidowDetails;

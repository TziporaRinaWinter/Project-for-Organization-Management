import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import WidowsList from "./WidowsList";
import WidowDetails from "./WidowDetails";

const AppWidow = () => {
  const { id } = useParams();
  const [selectedWidowId, setSelectedWidowId] = useState(id || null);

  useEffect(() => {
    setSelectedWidowId(id);
  }, [id]);

  const handleSelectWidow = (id) => {
    setSelectedWidowId(id);
  };

  return (
    <div>
      {selectedWidowId ? (
        <WidowDetails widowId={selectedWidowId} />
      ) : (
        <WidowsList onSelectWidow={handleSelectWidow} />
      )}
    </div>
  );
};
export default AppWidow;

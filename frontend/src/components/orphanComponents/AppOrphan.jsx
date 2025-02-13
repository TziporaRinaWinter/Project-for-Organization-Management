import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import OrphanList from "./OrphansList";
import OrphanDetails from "./OrphanDetails";

const AppOrphan = () => {
  const { id } = useParams();
  const [selectedOrphanId, setSelectedOrphanId] = useState(id || null);

  useEffect(() => {
    setSelectedOrphanId(id);
  }, [id]);

  const handleSelectOrphan = (id) => {
    setSelectedOrphanId(id);
  };

  return (
    <div>
      {selectedOrphanId ? (
        <OrphanDetails orphanId={selectedOrphanId} />
      ) : (
        <OrphanList onSelectOrphan={handleSelectOrphan} />
      )}
    </div>
  );
};
export default AppOrphan;

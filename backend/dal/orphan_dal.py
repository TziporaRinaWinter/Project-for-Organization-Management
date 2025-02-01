from db.DB_manager import DBManager
from dal.object_manager import ObjectManager
from models.models import Orphan, School


class OrphanDAL:
    def __init__(self, db_manager: DBManager):
        self.object_manager = ObjectManager(db_manager)

    def get_all_orphans(self):
        return self.object_manager.get_objects_whithout_rel(Orphan)

    def get_orphan_with_rel(self, orphan_id):
        relationships = ["school"]
        filters = [Orphan.id == orphan_id]
        return self.object_manager.get_objects(Orphan, Orphan.schema(), relationships=relationships, filters=filters)

    def get_orphan(self, orphan_id):
        filters = {"id": orphan_id}
        return self.object_manager.get_objects_whithout_rel(Orphan, filters)

    def create_orphan(self, orphan_data):
        orphan_info = {key: orphan_data[key] for key in orphan_data if key not in ['school']}
        # Build relationship dict
        relationships = {
            'school': (School, [orphan_data.get("school", {})]) if orphan_data.get("school") else None
        }
        # Calling the generic function to create the object with the relationships
        return self.object_manager.create_object(Orphan, orphan_info, relationships)

    def update_orphan(self, orphan_id, updates):
        filters = [Orphan.id == orphan_id]
        return self.object_manager.update_objects(Orphan, Orphan.schema(), filters, updates)
    
    def update_orphan(self, orphan_id, orphan_data):
        # Prepare the data for update
        orphan_info = {key: orphan_data[key] for key in orphan_data if key not in ['school']}
        # Build relationship dict
        relationships = {
            'school': (School, [orphan_data.get("school", {})]) if orphan_data.get("school") else None
        }
        # Calling the generic function to update the object with the relationships
        return self.object_manager.update_object(Orphan, orphan_id, orphan_info, relationships)

    def delete_orphan(self, orphan_id):
        filters = [Orphan.id == orphan_id]
        return self.object_manager.delete_objects(Orphan, filters)

    def delete_all_orphans(self):
        return self.object_manager.delete_objects(Orphan)

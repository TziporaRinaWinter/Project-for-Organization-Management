from db.DB_manager import DBManager
from dal.object_manager import ObjectManager
from models.models import Event, Orphan, Widow


class EventDAL:
    def __init__(self, db_manager: DBManager):
        self.object_manager = ObjectManager(db_manager)

    def get_all_events(self):
        return self.object_manager.get_objects_whithout_rel(Event)

    def get_event_with_rel(self, event_id):
        relationships = ["orphans", "widows"]
        filters = [Event.id == event_id]
        return self.object_manager.get_objects(Event, Event.schema(), relationships=relationships, filters=filters)

    def get_event(self, event_id):
        filters = {"id": event_id}
        return self.object_manager.get_objects_whithout_rel(Event, filters)

    def create_event(self, event_data):
        event_info = {key: event_data[key] for key in event_data if key not in ["orphans", "widows"]}
        # Build relationship dict
        relationships = {
            'widows': (Widow, [data for data in event_data.get('widows', [])]),
            'orphans': (Orphan, [data for data in event_data.get('orphans', [])])
        }
        # Calling the generic function to create the object with the relationships
        return self.object_manager.create_object(Event, event_info, relationships)

    def update_event(self, event_id, updates):
        filters = [Event.id == event_id]
        return self.object_manager.update_objects(Event, Event.schema(), filters, updates)
    
    def update_event(self, event_id, event_data):
        # Prepare the data for update
        event_info = {key: event_data[key] for key in event_data if key not in ["orphans", "widows"]}
        # Build relationship dict
        relationships = {
            'widows': (Widow, [data for data in event_data.get('widows', [])]),
            'orphans': (Orphan, [data for data in event_data.get('orphans', [])])
        }
        # Calling the generic function to update the object with the relationships
        return self.object_manager.update_object(Event, event_id, event_info, relationships)

    def delete_event(self, event_id):
        filters = [Event.id == event_id]
        return self.object_manager.delete_objects(Event, filters)

    def delete_all_events(self):
        return self.object_manager.delete_objects(Event)

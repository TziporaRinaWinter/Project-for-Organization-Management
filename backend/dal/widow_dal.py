from db.DB_manager import DBManager
from dal.object_manager import ObjectManager
from models.models import Widow, Orphan, Relative, Address, BankAccount


class WidowDAL:
    def __init__(self, db_manager: DBManager):
        self.object_manager = ObjectManager(db_manager)

    def get_all_widows(self):
        return self.object_manager.get_objects_whithout_rel(Widow)

    def get_widow_with_rel(self, widow_id):
        relationships = ["bank_account", "address", "orphans", "relatives"]
        filters = [Widow.id == widow_id]
        return self.object_manager.get_objects(Widow, Widow.schema(), relationships=relationships, filters=filters)

    def get_widow(self, widow_id):
        filters = {"id": widow_id}
        return self.object_manager.get_objects_whithout_rel(Widow, filters)

    def create_widow(self, widow_data):
        widow_info = {key: widow_data[key] for key in widow_data if
                      key not in ['orphans', 'relatives', 'address', 'bank_account']}
        # Build relationship dict
        relationships = {
            'orphans': (Orphan, [data for data in widow_data.get('orphans', [])]),
            'relatives': (Relative, [data for data in widow_data.get('relatives', [])]),
            'address': (Address, [widow_data.get("address", {})]) if widow_data.get("address") else None,
            'bank_account': (BankAccount, [widow_data.get("bank_account", {})]) if widow_data.get("bank_account") else None
        }
        # Calling the generic function to create the object with the relationships
        return self.object_manager.create_object(Widow, widow_info, relationships)

    def update_widow(self, widow_id, updates):
        filters = [Widow.id == widow_id]
        return self.object_manager.update_objects(Widow, Widow.schema(), filters, updates)
    
    def update_widow(self, widow_id, widow_data):
        # Prepare the data for update
        widow_info = {key: widow_data[key] for key in widow_data if
                      key not in ['orphans', 'relatives', 'address', 'bank_account']}
        # Build relationship dict
        relationships = {
            'orphans': (Orphan, [data for data in widow_data.get('orphans', [])]),
            'relatives': (Relative, [data for data in widow_data.get('relatives', [])]),
            'address': (Address, [widow_data.get("address", {})]) if widow_data.get("address") else None,
            'bank_account': (BankAccount, [widow_data.get("bank_account", {})]) if widow_data.get("bank_account") else None
        }
        # Calling the generic function to update the object with the relationships
        return self.object_manager.update_object(Widow, widow_id, widow_info, relationships)

    def delete_widow(self, widow_id):
        filters = [Widow.id == widow_id]
        return self.object_manager.delete_objects(Widow, filters)

    def delete_all_widows(self):
        return self.object_manager.delete_objects(Widow)

from db.DB_manager import DBManager
from dal.object_manager import ObjectManager
from models.models import Widow, Orphan, Relative
from models.schema import WidowSchema

from models.models import Address, BankAccount


class WidowDAL:
    def __init__(self, db_manager: DBManager):
        self.object_manager = ObjectManager(db_manager)

    def get_all_widows(self):
        return self.object_manager.get_objects_whithout_rel(Widow)

    def get_widow_with_rel(self, widow_id):
        relationships = ["bank_account", "address", "orphans", "relatives"]
        filters = [Widow.id == widow_id]
        return self.object_manager.get_objects(Widow, WidowSchema, relationships=relationships, filters=filters)

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
        return self.object_manager.update_objects(Widow, WidowSchema, filters, updates)
    
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
        return self.update_object(Widow, widow_id, widow_info, relationships)

    def delete_widow(self, widow_id):
        filters = [Widow.id == widow_id]
        return self.object_manager.delete_objects(Widow, filters)

    def delete_all_widows(self):
        return self.object_manager.delete_objects(Widow)


    
    # def create_widow(self, data: dict):
    #     # יצירת אובייקט אלמנה
    #     widow_data = {
    #         "identity_number": data["identity_number"],
    #         "first_name": data.get("first_name"),
    #         "last_name": data.get("last_name"),
    #         "home_phone": data.get("home_phone"),
    #         "mobile_phone": data.get("mobile_phone"),
    #         "email": data.get("email"),
    #         "birth_date": data.get("birth_date"),
    #         "widowhood_date": data.get("widowhood_date"),
    #         "num_of_minor_children": data.get("num_of_minor_children"),
    #         "num_of_unmarried_children": data.get("num_of_unmarried_children"),
    #     }

    #     # יצירת כתובת במידה וקיימת
    #     if data.get("address"):
    #         address_data = data["address"]
    #         widow_data["address"] = Address(
    #             city = address_data.get("city"),
    #             street = address_data.get("street"),
    #             num_building = address_data.get("num_building"),
    #         )
    #     #יצירת חשבון בנק במידה וקיים
    #     if data.get("bank_account"):
    #         bank_data = data["bank_account"]
    #         widow_data["bank_account"] = BankAccount(
    #             holder_name = bank_data.get("holder_name"),
    #             account_number = bank_data.get("account_number"),
    #             branch = bank_data.get("branch"),
    #             bank_number = bank_data.get("bank_number"),
    #         )

    #     # יצירת אובייקט
    #     widow = Widow(**widow_data)

    #     # הוספת ילדים
    #     for orphan in data.get("orphans", []):
    #         widow.orphans.append(
    #             Orphan(
    #                 identity_number = orphan.get("identity_number"),
    #                 first_name = orphan.get("first_name"),
    #                 last_name = orphan.get("last_name"),
    #                 birth_date = orphan.get("birth_date"),
    #                 gender = orphan.get("gender"),
    #                 age_group = orphan.get("age_group")
    #             )
    #         )
    #     #הוספת קרובי משפחה
    #     for relative in data.get("relatives", []):
    #         widow.relatives.append(
    #             Relative(
    #                 fl_name = relative.get("fl_name"),
    #                 phone = relative.get("phone"),
    #                 email = relative.get("email"),
    #                 relationship_type = relative.get("relationship_type"),
    #             )
    #         )

    #     with self.db_manager.get_session() as session:
    #         session.add(widow)
    #         session.commit()
    #         return widow

from dal.widow_dal import WidowDAL

class WidowBL:
    def __init__(self, widow_dal: WidowDAL):
        self.widow_dal = widow_dal

    def get_all_widows(self):
        return self.widow_dal.get_all_widows()

    def get_widow(self, widow_id):
        return self.widow_dal.get_widow(widow_id)

    def get_widow_with_rel(self, widow_id):
        return self.widow_dal.get_widow_with_rel(widow_id)

    def create_widow(self, widow_data):
        return self.widow_dal.create_widow(widow_data)

    def update_widow(self, widow_id, widow_data):
        return self.widow_dal.update_widow(widow_id, widow_data)

    def delete_widow(self, widow_id):
        return self.widow_dal.delete_widow(widow_id)

    def delete_all_widows(self):
        return self.widow_dal.delete_all_widows()

from dal.orphan_dal import OrphanDAL

class OrphanBL:
    def __init__(self, orphan_dal: OrphanDAL):
        self.orphan_dal = orphan_dal

    def get_all_orphans(self):
        return self.orphan_dal.get_all_orphans()

    def get_orphan(self, orphan_id):
        return self.orphan_dal.get_orphan(orphan_id)

    def get_orphan_with_rel(self, orphan_id):
        return self.orphan_dal.get_orphan_with_rel(orphan_id)

    def create_orphan(self, orphan_data):
        return self.orphan_dal.create_orphan(orphan_data)

    def update_orphan(self, orphan_id, orphan_data):
        return self.orphan_dal.update_orphan(orphan_id, orphan_data)

    def delete_orphan(self, orphan_id):
        return self.orphan_dal.delete_orphan(orphan_id)

    def delete_all_orphans(self):
        return self.orphan_dal.delete_all_orphans()

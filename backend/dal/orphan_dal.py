from sqlalchemy.orm import Session
from models import Orphan

class OrphanDAL:
    def __init__(self, session: Session):
        self.session = session

    def get_all_orphans(self):
        return self.session.query(Orphan).all()

    def get_orphan(self, orphan_id):
        return self.session.query(Orphan).filter(Orphan.id == orphan_id).first()

    def create_orphan(self, orphan_data):
        orphan = Orphan(**orphan_data)
        self.session.add(orphan)
        self.session.commit()
        return orphan

    def update_orphan(self, orphan_id, orphan_data):
        orphan = self.session.query(Orphan).filter(Orphan.id == orphan_id).first()
        if orphan:
            for key, value in orphan_data.items():
                setattr(orphan, key, value)
            self.session.commit()
        return orphan

    def delete_orphan(self, orphan_id):
        orphan = self.session.query(Orphan).filter(Orphan.id == orphan_id).first()
        if orphan:
            self.session.delete(orphan)
            self.session.commit()
        return orphan

    def delete_all_orphans(self):
        self.session.query(Orphan).delete()
        self.session.commit()

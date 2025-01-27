from sqlalchemy.orm import Session
from models import Event

class EventDAL:
    def __init__(self, session: Session):
        self.session = session

    def get_all_events(self):
        return self.session.query(Event).all()

    def get_event(self, event_id):
        return self.session.query(Event).filter(Event.id == event_id).first()

    def create_event(self, event_data):
        event = event(**event_data)
        self.session.add(event)
        self.session.commit()
        return event

    def update_event(self, event_id, event_data):
        event = self.session.query(Event).filter(Event.id == event_id).first()
        if event:
            for key, value in event_data.items():
                setattr(event, key, value)
            self.session.commit()
        return event

    def delete_event(self, event_id):
        event = self.session.query(Event).filter(Event.id == event_id).first()
        if event:
            self.session.delete(event)
            self.session.commit()
        return event

    def delete_all_events(self):
        self.session.query(Event).delete()
        self.session.commit()

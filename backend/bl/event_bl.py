from dal.event_dal import EventDAL

class EventBL:
    def __init__(self, event_dal: EventDAL):
        self.event_dal = event_dal

    def get_all_events(self):
        return self.event_dal.get_all_events()

    def get_event(self, event_id):
        return self.event_dal.get_event(event_id)

    def get_event_with_rel(self, event_id):
        return self.event_dal.get_event_with_rel(event_id)

    def create_event(self, event_data):
        return self.event_dal.create_event(event_data)

    def update_event(self, event_id, event_data):
        return self.event_dal.update_event(event_id, event_data)

    def delete_event(self, event_id):
        return self.event_dal.delete_event(event_id)

    def delete_all_events(self):
        return self.event_dal.delete_all_events()

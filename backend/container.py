from injector import Injector, Module, provider, singleton
from db.DB_manager import DBManager
from dal.widow_dal import WidowDAL
from bl.widow_bl import WidowBL
from dal.orphan_dal import OrphanDAL
from bl.orphan_bl import OrphanBL
from dal.event_dal import EventDAL
from bl.event_bl import EventBL
from fastapi import APIRouter

class AppModule(Module):
    @provider
    @singleton
    def provide_db_manager(self) -> DBManager:
        return DBManager()
    
class WidowModule(Module):
    @provider
    @singleton
    def provide_widow_dal(self, db_manager: DBManager) -> WidowDAL:
        return WidowDAL(db_manager)

    @provider
    @singleton
    def provide_widow_bl(self, widow_dal: WidowDAL) -> WidowBL:
        return WidowBL(widow_dal)

class OrphanModule(Module):
    @provider
    @singleton
    def provide_orphan_dal(self, db_manager: DBManager) -> OrphanDAL:
        return OrphanDAL(db_manager)

    @provider
    @singleton
    def provide_orphan_bl(self, orphan_dal: OrphanDAL) -> OrphanBL:
        return OrphanBL(orphan_dal)

class EventModule(Module):
    @provider
    @singleton
    def provide_event_dal(self, db_manager: DBManager) -> EventDAL:
        return EventDAL(db_manager)

    @provider
    @singleton
    def provide_event_bl(self, event_dal: EventDAL) -> EventBL:
        return EventBL(event_dal)

injector = Injector([AppModule, WidowModule, OrphanModule, EventModule])

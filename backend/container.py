from injector import Injector, Module, provider, singleton
from db.DB_manager import DBManager
from dal.widow_dal import WidowDAL
from bl.widow_bl import WidowBL

class AppModule(Module):
    @provider
    @singleton
    def provide_db_manager(self) -> DBManager:
        return DBManager()

    @provider
    @singleton
    def provide_widow_dal(self, db_manager: DBManager) -> WidowDAL:
        return WidowDAL(db_manager)

    @provider
    @singleton
    def provide_widow_bl(self, widow_dal: WidowDAL) -> WidowBL:
        return WidowBL(widow_dal)

injector = Injector([AppModule])

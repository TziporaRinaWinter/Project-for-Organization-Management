from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from env import ENV

class DBManager:
    def __init__(self):
        self.engine = create_engine(
            ENV().get_path_postgresql(),
            pool_pre_ping=True,
        )
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    @contextmanager
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_tables(self, base):
        base.metadata.create_all(self.engine, checkfirst=True)


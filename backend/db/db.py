from DB_manager import DBManager
# from models.models import Base
from sqlalchemy import text

def main():
    db_manager = DBManager()
    # db_manager.create_tables(Base)

    with db_manager.get_session() as session:
        session.execute(text('ALTER TABLE orphans ADD COLUMN hebrew_birth_date TEXT;'))


if __name__ == '__main__':
    main()

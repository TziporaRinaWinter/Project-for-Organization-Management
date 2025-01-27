from DB_manager import DBManager
from models.models import Base

def main():
    db_manager = DBManager()
    db_manager.create_tables(Base)

if __name__ == '__main__':
    main()

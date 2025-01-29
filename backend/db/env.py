import os
from dotenv import load_dotenv

class ENV:
    def __init__(self):
        load_dotenv()

        self.username = os.getenv("USER_NAME")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")
        self.database_name = os.getenv("DATABASE_NAME")



    def get_path_postgresql(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database_name}"

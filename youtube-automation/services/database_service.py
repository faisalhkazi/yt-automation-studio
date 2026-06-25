import sqlite3
from pathlib import Path

DB_PATH = Path("database/database.db")


class DatabaseService:

    @staticmethod
    def connect():
        return sqlite3.connect(DB_PATH)

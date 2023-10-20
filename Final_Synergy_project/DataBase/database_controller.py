import sqlite3
from typing import List, Tuple
from DataBase.database_commands import *

class database():
    def __init__(self) -> None:
        self.conn = sqlite3.connect('Company.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Staff(
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                second_name TEXT,
                last_name TEXT,
                phone_number TEXT,
                email TEXT,
                salary REAL
            ); 
            """)
        self.conn.commit()

    def create_staff(self, data : List[str | float]) -> None:
        self.cur.execute(create_command, tuple(data))
        self.conn.commit()

    def delete_staff(self, identifier : int) -> None:
        self.cur.execute(delete_command, (identifier, ))
        self.conn.commit()

    def update_staff(self, data : List[str | float]) -> None:
        self.cur.execute(update_command, tuple(data))
        self.conn.commit()

    def find_staff(self, data : List[str | float]) -> Tuple [Tuple [str]]:
        self.cur.execute(find_by_FCs, tuple(data))
        return self.cur.fetchall()
    
    def find_all_staff(self) -> Tuple [Tuple [str]]:
        self.cur.execute(find_all_data)
        return self.cur.fetchall()
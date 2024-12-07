import sqlite3
from sqlite3 import Connection, Cursor

class GenericDAO:
    def __init__(self):
        self._conn = sqlite3.connect("./database/banco.db")
        self._cursor = self._conn.cursor()

    @property
    def conn(self) -> Connection:
        return self._conn
    
    @property
    def cursor(self) -> Cursor:
        return  self._cursor
    
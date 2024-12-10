import sqlite3
from sqlite3 import Connection, Cursor

class GenericDAO:
    def __init__(self):
        self._conn = sqlite3.connect("./database/banco.db")
        self._cursor = self._conn.cursor()
        # HABILITA FKs PARA A SESSÃO COM O COMANDO PRAGMA
        self._cursor.execute(
            '''PRAGMA foreign_keys = ON'''
        )

    @property
    def conn(self) -> Connection:
        return self._conn
    
    @property
    def cursor(self) -> Cursor:
        return  self._cursor
    
    def __enter__(self): 
        return self
    
    def __exit__(self, exec_type, exec_val, exec_tb):
        if (self._cursor): self._cursor.close()
        if (self._conn): self._conn.close()
    
    
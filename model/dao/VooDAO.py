from typing import Union
from sqlite3 import IntegrityError
from .GenericDAO import GenericDAO
from model.entity.Voo import Voo
from exceptions.RegisterNotFoundException import RegisterNotFoundException

class VooDAO(GenericDAO):
    def __init__(self):
        super().__init__()

    def insert(self, voo: Voo) -> None:
        self.cursor.execute(
            '''INSERT INTO Voo(origem, destino, data) VALUES
            (?, ?, ?)
            ''',
            [voo.origem, voo.destino, voo.data]
        )

        self.conn.commit()

    def getById(self, id: int) -> Voo:
        
        try:
            self.cursor.execute(
                '''SELECT * FROM Voo WHERE id = ?''',
                [id]
            )
            data = self.cursor.fetchone()
            voo = Voo(id=data[0], origem=data[1], destino=data[2], data=data[3])
            return voo
        except TypeError:
            raise RegisterNotFoundException("VOO NÃO ENCONTRADO")
        
    def delete(self, id: int) -> bool:
        try: 
            self.cursor.execute("DELETE FROM Voo WHERE id = ?", [id])
            self.conn.commit()
            return True
        except IntegrityError:
            return False
        
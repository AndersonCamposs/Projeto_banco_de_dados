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
            '''INSERT INTO Voo(cod, origem, destino, data) VALUES
            (?, ?, ?, ?)
            ''',
            [voo.cod, voo.origem, voo.destino, voo.data]
        )

        self.conn.commit()

    def getById(self, id: int) -> Voo:
        
        try:
            self.cursor.execute(
                '''SELECT * FROM Voo WHERE id = ?''',
                [id]
            )
            data = self.cursor.fetchone()
            voo = Voo(id=data[0], cod=data[1], origem=data[2], destino=data[3], data=data[4])
            return voo
        except TypeError:
            raise RegisterNotFoundException("VOO NÃO ENCONTRADO")
        
    def getByCod(self, cod: str):
        try:
            self.cursor.execute(
                '''SELECT * FROM Voo WHERE cod = ?''',
                [cod]
            )
            data = self.cursor.fetchone()
            voo = Voo(id=data[0], cod=data[1], origem=data[2], destino=data[3], data=data[4])
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
        
    def listAll(self) -> list[Voo]:
        try:
            self.cursor.execute("SELECT * FROM Voo")
            data = self.cursor.fetchall()

            listaVoos = []
            
            for registro in data:
                listaVoos.append(Voo(registro[0], registro[1], registro[2], registro[3], registro[4]))

            if(len(listaVoos) != 0):
                return listaVoos
            else:
                raise RegisterNotFoundException("NÃO HÁ REGISTROS")
        except TypeError:
            raise TypeError("ERRO AO CARREGAR A LISTA")

        
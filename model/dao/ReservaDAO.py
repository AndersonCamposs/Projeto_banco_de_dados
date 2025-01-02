from typing import Union
from .GenericDAO import GenericDAO
from .VooDAO import VooDAO
from .ClienteDAO import ClienteDAO
from model.entity.Reserva import Reserva
from exceptions.RegisterNotFoundException import RegisterNotFoundException

class ReservaDAO(GenericDAO):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, reserva: Reserva):
        self.cursor.execute(
            '''INSERT INTO Reserva (cod, idCliente, idVoo, data, valor)
            VALUES (?, ?, ?, ?, ?)''',
            [reserva.cod, reserva.cliente, reserva.voo, reserva.data, reserva.valor]
        )
        self.conn.commit()

    def getById(self, id: int) -> Reserva:

        try:
            self.cursor.execute(
                '''SELECT * FROM Reserva WHERE id = ?''',
                [id]
            )
            data = self.cursor.fetchone()

            reserva = Reserva(id=data[0], cod=data[1],cliente=ClienteDAO().getById(int(data[2])), voo=VooDAO().getById(int(data[3])), data=data[4], valor=data[5])
            return reserva
        except TypeError:
            raise RegisterNotFoundException("RESERVA NÃO ENCONTRADA")
        
    def getByCod(self, cod: str):
        try:
            self.cursor.execute(
                '''SELECT * FROM Reserva WHERE cod = ?''',
                [cod]
            )
            data = self.cursor.fetchone()
            reserva = Reserva(id=data[0], cod=data[1],cliente=ClienteDAO().getById(int(data[2])), voo=VooDAO().getById(int(data[3])), data=data[4], valor=data[5])
            return reserva
        except TypeError:
            raise RegisterNotFoundException("RESERVA NÃO ENCONTRADA")
        
    def listByVooId(self, idVoo: int) -> Union[list[Reserva], None]:
        try:
            self.cursor.execute(
                '''SELECT * FROM Reserva WHERE idVoo = ?''',
                [idVoo]
            )
            data = self.cursor.fetchall()
            
            listaReservas = []
            
            for registro in data:
                reserva = Reserva(id=registro[0], cod=registro[1], cliente=ClienteDAO().getById(int(registro[2])), voo=VooDAO().getById(int(registro[3])), data=registro[4], valor=registro[5])
                listaReservas.append(reserva)
            
            if(len(listaReservas) != 0):
                return listaReservas
            else:
                raise RegisterNotFoundException("NÃO EXISTEM RESERVAS PARA ESTE VOO")
        except TypeError:
            raise TypeError("ERRO AO CARREGAR A LISTA")
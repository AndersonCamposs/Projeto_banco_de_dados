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
            '''INSERT INTO Reserva (idCliente, idVoo, data, valor)
            VALUES (?, ?, ?, ?)''',
            [reserva.cliente, reserva.voo, reserva.data, reserva.valor]
        )
        self.conn.commit()

    def getById(self, id: int) -> Reserva:

        try:
            self.cursor.execute(
                '''SELECT * FROM Reserva WHERE id = ?''',
                [id]
            )
            data = self.cursor.fetchone()
            reserva = Reserva(id=data[0], cliente=ClienteDAO().getById(int(data[1])), voo=VooDAO().getById(int(data[2])), data=data[3], valor=data[4])
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
                reserva = Reserva(id=registro[0], cliente=ClienteDAO().getById(int(registro[1])), voo=VooDAO().getById(int(registro[2])), data=registro[3], valor=registro[4])
                listaReservas.append(reserva)
            return listaReservas
        except TypeError:
            return None
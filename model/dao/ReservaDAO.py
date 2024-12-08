from typing import Union
from .GenericDAO import GenericDAO
from model.entity.Reserva import Reserva

class ReservaDAO(GenericDAO):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, reserva: Reserva):
        self.cursor.execute(
            '''INSERT INTO Reserva (idCliente, idVoo, data, valor)
            VALUES (?, ?, ?, ?)''',
            [reserva.idCliente, reserva.idVoo, reserva.data, reserva.valor]
        )
        self.conn.commit()

    def getById(self, id: int) -> Union[Reserva, None]:

        try:
            self.cursor.execute(
                '''SELECT * FROM Reserva WHERE id = ?''',
                [id]
            )
            data = self.cursor.fetchone()
            reserva = Reserva(id=data[0], idCliente=data[1], idVoo=data[2], data=data[3], valor=data[4])
            return reserva
        except TypeError:
            return None
        
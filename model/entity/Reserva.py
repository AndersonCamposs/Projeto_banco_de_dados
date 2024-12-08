from typing import Union

class Voo:
    def __init__(self, id: Union[int, None], idCliente: int, idVoo: int, data: str, valor: float ):
        self._id = id
        self._idCliente = idCliente
        self._idVoo = idVoo
        self._data = data
        self._valor = valor

    @property
    def id(self) -> Union[int, None]:
        return self._id
    
    @property
    def idCliente(self) -> str:
        return self._idCliente
    @idCliente.setter
    def idCliente(self, novoidCliente: int) -> None:
        self._idCliente = novoidCliente

    @property
    def idVoo(self) -> str:
        return self._idVoo
    @idVoo.setter
    def idVoo(self, novoidVoo: int) -> None:
        self._idCliente = novoidVoo

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, novaData: str):
        self._data = novaData

    @property
    def valor(self) -> float:
        return self._valor
    @valor.setter
    def valor(self, novoValor: float)
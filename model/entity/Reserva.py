from typing import Union
from .Voo import Voo
from .Cliente import Cliente

class Reserva:
    def __init__(self, id: Union[int, None],cod: str, cliente: Cliente, voo: Voo, data: str, valor: float ):
        self._id = id
        self._cod = cod
        self._cliente = cliente
        self._voo = voo
        self._data = data
        self._valor = valor

    @property
    def id(self) -> Union[int, None]:
        return self._id
    
    @property
    def cod(self) -> str:
        return self._cod
    @cod.setter
    def cod(self, novoCod):
        self._cod = novoCod
    
    @property
    def cliente(self) -> Cliente:
        return self._cliente
    @cliente.setter
    def cliente(self, cliente: Cliente) -> None:
        self._cliente = cliente
    @property
    def voo(self) -> Voo:
        return self._voo
    @voo.setter
    def voo(self, voo: Voo) -> None:
        self._voo = voo

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
    def valor(self, novoValor: float): 
        self._valor = novoValor
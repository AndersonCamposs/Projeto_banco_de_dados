from typing import Union

class Voo:
    def __init__(self, id: Union[int, None], origem: str, destino: str, data: str ):
        self._id = id
        self._origem = origem
        self._destino = destino
        self._data = data

    @property
    def id(self) -> Union[int, None]:
        return self._id
    
    @property
    def origem(self) -> str:
        return self._origem
    @origem.setter
    def origem(self, novaOrigem: str) -> None:
        self._origem = novaOrigem

    @property
    def destino(self) -> str:
        return self._destino
    @destino.setter
    def destino(self, novoDestino: str) -> None:
        self._origem = novoDestino

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, novaData: str):
        self._data = novaData
from model.dao.VooDAO import VooDAO
from model.entity.Voo import Voo
from utils.Validator import Validator

class VooService:
    def __init__(self):
        self._vooDAO = VooDAO()

    @property
    def vooDAO(self) -> VooDAO:
        return self._vooDAO
    
    def cadastrarVoo(self, origem: str, destino: str, data: str) -> None:
        Validator.dateValidation(data)

        self._vooDAO.insert(Voo(None, origem, destino, data))

    def deletarVoo(self, id:int):
        self._vooDAO.getById(id)
        self._vooDAO.delete(id)
        
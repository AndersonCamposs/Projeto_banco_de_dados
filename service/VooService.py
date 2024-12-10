from model.dao.VooDAO import VooDAO
from model.entity.Voo import Voo
from utils.Validator import Validator

class VooService:
    def __init__(self):
        pass

    def cadastrarVoo(self, origem: str, destino: str, data: str) -> None:
        Validator.dateValidation(data)
        with VooDAO() as vooDAO:
            vooDAO.insert(Voo(None, origem, destino, data))

    def deletarVoo(self, id:int):
        with VooDAO() as vooDAO:
            self._vooDAO.getById(id)
            self._vooDAO.delete(id)

    def buscarPorId(self, id: int):
        with VooDAO() as vooDAO:
            return vooDAO.getById(id)
        
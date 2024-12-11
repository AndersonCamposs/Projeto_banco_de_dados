from model.dao.VooDAO import VooDAO
from model.entity.Voo import Voo
from utils.Validator import Validator

class VooService:
    def __init__(self):
        pass

    def cadastrarVoo(self, cod, origem: str, destino: str, data: str) -> None:
        Validator.dateValidation(data)
        with VooDAO() as vooDAO:
            vooDAO.insert(Voo(None, cod, origem, destino, data))

    def deletarVoo(self, cod: str):
        with VooDAO() as vooDAO:
            voo = vooDAO.getByCod(cod)
            vooDAO.delete(voo.id)

    def buscarPorId(self, id: int):
        with VooDAO() as vooDAO:
            return vooDAO.getById(id)
        
    def buscarPorCod(self, cod: str):
        with VooDAO() as vooDAO:
            return vooDAO.getByCod(cod)
        
    def listarVoos(self):
        with VooDAO() as vooDAO:
            return vooDAO.listAll()
        
from service.VooService import VooService
from utils.Validator import Validator


class VooController:
    def __init__(self):
        self._vooService = VooService()

    @property
    def vooService(self):
        return self._vooService
    
    def cadastraVoo(self, origem: str, destino: str, data: str) -> str:
        Validator.dateValidation(data)
        return self.vooService.cadastrarVoo(origem, destino, data)

    def relatorioVoo(self, cod: str):
        return self._vooService.buscarPorCod(cod)
        
    def deletarVoo(self, cod: str):
        return self._vooService.deletarVoo(cod)
            
    def listarVoos(self):
        return self._vooService.listarVoos()
            
        
                
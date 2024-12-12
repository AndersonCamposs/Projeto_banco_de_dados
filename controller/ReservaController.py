from service.ReservaService import ReservaService
from service.ClienteService import ClienteService
from service.VooService import VooService
from utils.Validator import Validator


class ReservaController:
    def __init__(self):
        self._reservaService = ReservaService()
        self._clienteService = ClienteService()
        self._vooService = VooService()

    @property
    def reservaService(self):
        return self._reservaService
    
    @property
    def clienteService(self):
        return self._clienteService
    
    @property
    def vooService(self):
        return self._vooService
    
    def cadastrarReserva(self, cpfCliente, codVoo, valor): 
        Validator.cpfValidation(cpfCliente)
        return self._reservaService.cadastrarReserva(cpfCliente, codVoo, valor)

    def relatorioReserva(self, cod):
        return self._reservaService.buscarPorCod(cod)
        

    def listarReservasVoo(self, cod):
        voo = self._vooService.buscarPorCod(cod)
        return self._reservaService.listarPorVoo(voo.id)
            
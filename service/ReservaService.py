from datetime import date
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from model.dao.ClienteDAO import ClienteDAO
from model.dao.ReservaDAO import ReservaDAO
from model.dao.VooDAO import VooDAO
from model.entity.Reserva import Reserva


class ReservaService:
    def __init__(self):
        self._reservaDAO = ReservaDAO()

    @property
    def reservaDAO(self):
        return self._reservaDAO
    
    def cadastrarReserva(self, cpfCliente, idVoo, valor):
        cliente = ClienteDAO().getByCpf(cpfCliente)          
        voo = VooDAO().getById(idVoo)

        self._reservaDAO.insert(Reserva(None, cliente.id, voo.id, date.today().strftime("%d/%m/%Y"), valor))

    def listarPorVoo(self, idVoo: int):
        lista = self._reservaDAO.listByVooId(idVoo)
        if (lista): 
            return lista
        else:
            raise RegisterNotFoundException("NÃO EXISTEM RESERVAS PARA ESSE VOO")

    def buscarPorId(self, id: int):
        return self._reservaDAO.getById(id)
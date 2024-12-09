from datetime import date
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

        self._reservaDAO.insert(Reserva(None, cliente.id, voo.id, date.today().strftime("%d/%m/%Y")))
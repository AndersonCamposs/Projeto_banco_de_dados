from datetime import date
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from model.dao.ClienteDAO import ClienteDAO
from model.dao.ReservaDAO import ReservaDAO
from model.dao.VooDAO import VooDAO
from model.entity.Reserva import Reserva


class ReservaService:
    def __init__(self):
        pass
    
    def cadastrarReserva(self, cod,cpfCliente, codVoo, valor):
        with ClienteDAO() as clienteDAO, VooDAO() as vooDAO, ReservaDAO() as reservaDAO:
            cliente = clienteDAO.getByCpf(cpfCliente)          
            voo = vooDAO.getByCod(codVoo)

            reservaDAO.insert(Reserva(None, cod, cliente.id, voo.id, date.today().strftime("%d/%m/%Y"), valor))

    def listarPorVoo(self, idVoo: int) -> list[Reserva]:
        with ReservaDAO() as reservaDAO, VooDAO() as vooDAO:
            return reservaDAO.listByVooId(idVoo)

    def buscarPorId(self, id: int):
        with ReservaDAO() as reservaDAO:
            return reservaDAO.getById(id)
        
    def buscarPorCod(self, cod: str):
        with ReservaDAO() as reservaDAO:
            return reservaDAO.getByCod(cod)
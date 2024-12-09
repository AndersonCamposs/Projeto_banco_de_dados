from prettytable import PrettyTable
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from model.dao.ClienteDAO import ClienteDAO
from model.dao.ReservaDAO import ReservaDAO
from model.dao.VooDAO import VooDAO
from service.ReservaService import ReservaService
from utils.MessageManager import MessageManager


class ReservaController:
    def __init__(self):
        self._reservaService = ReservaService()

    @property
    def reservaService(self):
        return self._reservaService
    
    def cadastrarReserva(self):
        print("============================")
        cpfCliente = input("INFORME O CPF DO CLIENTE: ")
        idVoo = input("INFORME O ID DO VOO: ")
        try:
            
            try:
                valor = float(input("INFORME O VALOR DA RESERVA: "))
                
                self.reservaService.cadastrarReserva(cpfCliente, idVoo, valor)
                MessageManager.customMessage("RESERVA CADASTRADA COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)
            
            except ValueError:
                MessageManager.customMessage("VALOR DA RESERVA INVÁLIDO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
            
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

    def relatorioReserva(self):
        id = input("INFORME O ID DA RESERVA: ")
        try:
            reserva = ReservaDAO().getById(id)
            cliente = ClienteDAO().getById(reserva.idCliente)
            voo = VooDAO().getById(reserva.idVoo)
            table = PrettyTable()
            table.field_names = ["ID DA RESERVA", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
            table.add_row([reserva.id, cliente.nome, cliente.cpf, cliente.email, voo.origem, voo.destino, voo.data, reserva.data, reserva.valor])
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

    def listarReservasVoo(self):
        print("============================")
        idVoo = input("INFORME O ID DO VOO: ")
        try:
            VooDAO().getById(int(idVoo))
        
            listaReservas = ReservaDAO().listByVooId(idVoo)
            table = PrettyTable()
            table.field_names = ["ID DA RESERVA", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
            for reserva in listaReservas:
                table.add_row([reserva.id, reserva.cliente.nome, reserva.cliente.cpf, reserva.cliente.email, reserva.voo.origem, reserva.voo.destino, reserva.voo.data, reserva.data, reserva.valor], divider=True)

            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)


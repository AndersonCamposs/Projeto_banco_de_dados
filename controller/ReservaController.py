from prettytable import PrettyTable
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from exceptions.InvalidPatternException import InvalidPatternException
from model.dao.ClienteDAO import ClienteDAO
from model.dao.ReservaDAO import ReservaDAO
from model.dao.VooDAO import VooDAO
from service.ReservaService import ReservaService
from service.ClienteService import ClienteService
from service.VooService import VooService
from utils.MessageManager import MessageManager


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
    
    def cadastrarReserva(self):
        print("============================")
        cpfCliente = input("INFORME O CPF DO CLIENTE: ")
        codVoo = input("INFORME O CÓDIGO DO VOO: ")
        codReserva = input("INFORME O CÓDIGO DA RESERVA: ")
        try:  
            valor = float(input("INFORME O VALOR DA RESERVA: "))
            self._reservaService.cadastrarReserva(codReserva, cpfCliente, codVoo, valor)
            MessageManager.customMessage("RESERVA CADASTRADA COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.SUCCESS)
            
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)
        
        except InvalidPatternException as e:
            MessageManager.customMessage("VALOR DA RESERVA INVÁLIDO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)    

        except ValueError:
            MessageManager.customMessage("VALOR DA RESERVA INVÁLIDO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)    


    def relatorioReserva(self):
        cod = input("INFORME O CÓDIGO DA RESERVA: ")
        try:
            reserva = self._reservaService.buscarPorCod(cod)
            cliente = reserva.cliente
            voo = reserva.voo
            table = PrettyTable()
            table.field_names = ["ID DA RESERVA", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
            table.add_row([reserva.id, cliente.nome, cliente.cpf, cliente.email, voo.origem, voo.destino, voo.data, reserva.data, reserva.valor])
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def listarReservasVoo(self):
        print("============================")
        codVoo = input("INFORME O CÓDIGO DO VOO: ")
        try:
            voo = self._vooService.buscarPorCod(codVoo)
        
            listaReservas = self._reservaService.listarPorVoo(voo.id)
            table = PrettyTable()
            table.field_names = ["ID DA RESERVA", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
            for reserva in listaReservas:
                table.add_row([reserva.id, reserva.cliente.nome, reserva.cliente.cpf, reserva.cliente.email, reserva.voo.origem, reserva.voo.destino, reserva.voo.data, reserva.data, reserva.valor], divider=True)

            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)


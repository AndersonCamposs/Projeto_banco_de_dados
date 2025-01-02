from prettytable import PrettyTable
from controller.ReservaController import ReservaController
from exceptions.InvalidPatternException import InvalidPatternException
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from utils.Menu import Menu
from utils.MessageManager import MessageManager


class ReservaView:
    def __init__(self):
        self._reservaController = ReservaController()
        Menu.menuReserva()

    @property
    def reservaController(self):
        return self._reservaController
    
    def formularioInserir(self):
        print("============================")
        cpfCliente = input("INFORME O CPF DO CLIENTE: ")
        codVoo = input("INFORME O CÓDIGO DO VOO: ")
        try:
            valor = float(input("INFORME O VALOR DA RESERVA: "))
            cod = self._reservaController.cadastrarReserva(cpfCliente, codVoo, valor)
            MessageManager.customMessage(F"RESERVA DE CÓDIGO {cod} CADASTRADA COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.SUCCESS)
            
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)
        
        except InvalidPatternException as e:
            MessageManager.customMessage("VALOR DA RESERVA INVÁLIDO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)    

        except ValueError:
            MessageManager.customMessage("VALOR DA RESERVA INVÁLIDO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)    

    def formularioRelatorio(self):
        cod = input("INFORME O CÓDIGO DA RESERVA: ")
        try:
            reserva = self._reservaController.relatorioReserva(cod)
            cliente = reserva.cliente
            voo = reserva.voo
            table = PrettyTable()
            table.field_names = ["CÓD", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
            table.add_row([reserva.cod, cliente.nome, cliente.cpf, cliente.email, voo.origem, voo.destino, voo.data, reserva.data, reserva.valor])
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def exibirTodosPorVoo(self):
        print("============================")
        codVoo = input("INFORME O CÓDIGO DO VOO: ")
        try:
            listaReservas = self._reservaController.listarReservasVoo(codVoo)
            table = PrettyTable()
            table.field_names = ["CÓD DA RESERVA", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
            for reserva in listaReservas:
                table.add_row([reserva.cod, reserva.cliente.nome, reserva.cliente.cpf, reserva.cliente.email, reserva.voo.origem, reserva.voo.destino, reserva.voo.data, reserva.data, reserva.valor], divider=True)

            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

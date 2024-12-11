from prettytable import PrettyTable
from controller.ClienteController import ClienteController
from exceptions.InvalidPatternException import InvalidPatternException
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from utils.Menu import Menu
from utils.MessageManager import MessageManager


class ClienteView():
    def __init__(self):
        self._clienteController = ClienteController()
        Menu.menuCliente()

    @property
    def clienteController(self):
        return self._clienteController
    
    def formularioInserir(self):
        print("============================")
        try:
            nome = input("INFORME O NOME DO CLIENTE: ")
            cpf = input("INFORME O CPF DO CLIENTE(xxx.xxx.xxx-xx): ")
            dataNascimento = input("INFORME A DATA DE NASCIMENTO(dd/mm/aaaa): ")
            email = input("INFORME O E-MAIL DO CLIENTE: ")
            celular = input("INFORME O CELULAR DO CLIENTE: ")
            self._clienteController.cadastrarCliente(nome, cpf, dataNascimento, email, celular)

            MessageManager.customMessage("CLIENTE CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.SUCCESS)

        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def formularioRelatorio(self):
        print("============================")
        cpf = input("INFORME O CPF DO CLIENTE: ")
        try :
            cliente = self._clienteController.relatorioCliente(cpf)
            table = PrettyTable()
            table.field_names = ["ID", "NOME", "CPF", "DATA DE NASCIMENTO", "E-MAIL", "CELULAR"]
            table.add_row([cliente.id, cliente.nome, cliente.cpf, cliente.dataNascimento, cliente.email, cliente.celular])
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def formularioAtualizar(self):
        Menu.menuClienteAtualizar()
        opcao = input("INFORME A OPÇÃO DESEJADA: ")
        cpf = input("INFORME O CPF DO CLIENTE: ")
        try:
            if(opcao == "1" or opcao == "2"):
                if(opcao == "1"):
                    email = input("INFORME O NOVO E-MAIL DO CLIENTE: ")
                    self._clienteController.atualizarCliente(cpf, email, None)
                elif(opcao == "2"):
                    celular = input("INFORME O NOVO CELULAR DO CLIENTE: ")
                    self._clienteController.atualizarCliente(cpf, None, celular)
                MessageManager.customMessage("CLIENTE ATUALIZADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.SUCCESS)
            else:
                MessageManager.invalidOption()
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def exibirTodos(self):
        try:
            listaClientes = self._clienteController.listarClientes()        
            table = PrettyTable()
            table.field_names = ["ID", "NOME", "CPF", "DATA DE NASCIMENTO", "E-MAIL", "CELULAR"]
            for cliente in listaClientes:
                table.add_row([cliente.id, cliente.nome, cliente.cpf, cliente.dataNascimento, cliente.email, cliente.celular], divider=True)
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)

        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

        except TypeError as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)
                

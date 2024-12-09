from prettytable import PrettyTable
from exceptions.InvalidPatternException import InvalidPatternException
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from service.ClienteService import ClienteService
from utils.MessageManager import MessageManager

class ClienteController:
    def __init__(self):
        self._clienteService = ClienteService()

    @property
    def clienteService(self):
        return self._clienteService
    
    def cadastrarCliente(self):
        print("============================")
        try:
            nome = input("INFORME O NOME DO CLIENTE: ")
            cpf = input("INFORME O CPF DO CLIENTE(xxx.xxx.xxx-xx): ")
            dataNascimento = input("INFORME A DATA DE NASCIMENTO(dd/mm/aaaa): ")
            email = input("INFORME O E-MAIL DO CLIENTE: ")
            celular = input("INFORME O CELULAR DO CLIENTE: ")

            self._clienteService.cadastrarCliente(nome, cpf, dataNascimento, email, celular)
            MessageManager.customMessage("CLIENTE CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.SUCCESS)

        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def relatorioCliente(self):
        print("============================")
        cpf = input("INFORME O CPF DO CLIENTE: ")
        try :
            cliente = self._clienteService.buscarPorCpf(cpf)
            table = PrettyTable()
            table.field_names = ["ID", "NOME", "CPF", "DATA DE NASCIMENTO", "E-MAIL", "CELULAR"]
            table.add_row([cliente.id, cliente.nome, cliente.cpf, cliente.dataNascimento, cliente.email, cliente.celular])
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)
        
        

    def atualizarCliente(self, opcao: str):
        cpf = input("INFORME O CPF DO CLIENTE: ")
        try:
            cliente = self._clienteService.buscarPorCpf(cpf)
            if(opcao == "1"):
                email = input("INFORME O NOVO E-MAIL DO CLIENTE: ")
                self._clienteService.atualizarCliente(cliente.id, email, None)
            elif(opcao == "2"):
                celular = input("INFORME O NOVO CELULAR DO CLIENTE: ")
                self._clienteService.atualizarCliente(cliente.id, None, celular)
            
            MessageManager.customMessage("CLIENTE ATUALIZADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.SUCCESS)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def listarClientes(self):
        try:
            listaClientes = self._clienteService.listarClientes()
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
                
        
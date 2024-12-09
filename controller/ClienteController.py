from prettytable import PrettyTable
from exceptions.InvalidPatternException import InvalidPatternException
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from model.dao.ClienteDAO import ClienteDAO
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
            cpf = input("INFORME O CPF DO CLIENTE: ")
            dataNascimento = input("INFORME A DATA DE NASCIMENTO(dd/mm/aaaa): ")
            email = input("INFORME O E-MAIL DO CLIENTE: ")
            celular = input("INFORME O CELULAR DO CLIENTE: ")

            self.clienteService.cadastrarCliente(nome, cpf, dataNascimento, email, celular)
            MessageManager.customMessage("CLIENTE CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)

        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

    def relatorioCliente(self):
        print("============================")
        cpf = input("INFORME O CPF DO CLIENTE: ")
        cliente = ClienteDAO().getByCpf(cpf)
        if(cliente != None):
            table = PrettyTable()
            table.field_names = ["ID", "NOME", "CPF", "DATA DE NASCIMENTO", "E-MAIL", "CELULAR"]
            table.add_row([cliente.id, cliente.nome, cliente.cpf, cliente.dataNascimento, cliente.email, cliente.celular])
            print(table)
        else:
            MessageManager.customMessage("CLIENTE ENCONTRADO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
        
        MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)

    def atualizarCliente(self, opcao: str):
        cpf = input("INFORME O CPF DO CLIENTE: ")
        try:
            cliente = ClienteDAO().getByCpf(cpf)
            if(opcao == "1"):
                email = input("INFORME O NOVO E-MAIL DO CLIENTE: ")
                self.clienteService.atualizarCliente(cliente.id, email, None)
            elif(opcao == "2"):
                celular = input("INFORME O NOVO CELULAR DO CLIENTE: ")
                self.clienteService.atualizarCliente(cliente.id, None, celular)
            
            MessageManager.customMessage("CLIENTE ATUALIZADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
import sys
import os
from datetime import date
from prettytable import PrettyTable
from utils.Menu import Menu
from utils.MessageManager import MessageManager
from model.dao.ClienteDAO import ClienteDAO
from model.dao.VooDAO import VooDAO
from model.dao.ReservaDAO import ReservaDAO
from model.entity.Cliente import Cliente
from model.entity.Voo import Voo
from model.entity.Reserva import Reserva
from services.ClienteService import ClienteService
from exceptions.InvalidPatternException import InvalidPatternException

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class CompanhiaAerea:

    clienteService = ClienteService()

    @staticmethod
    def main():
        while True:
            Menu.menuPrincipal()
            opcao = input("INFORME A OPÇÃO DESEJADA: ")

            if(opcao == "0"):
                return

            elif(opcao == "1"): 
                os.system("cls")
                Menu.menuCliente()
                opcao = input("INFORME A OPÇÃO DESEJADA: ")
                if(opcao == "0"):
                    os.system("cls")
                    continue
                
                elif (opcao == "1"):
                    print("============================")
                    try:
                        nome = input("INFORME O NOME DO CLIENTE: ")
                        cpf = input("INFORME O CPF DO CLIENTE: ")
                        dataNascimento = input("INFORME A DATA DE NASCIMENTO(dd/mm/aaaa): ")
                        email = input("INFORME O E-MAIL DO CLIENTE: ")
                        celular = input("INFORME O CELULAR DO CLIENTE: ")

                        CompanhiaAerea.clienteService.cadastrarCliente(nome, cpf, dataNascimento, email, celular)
                        MessageManager.customMessage("CLIENTE CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)

                    except InvalidPatternException as e:
                        MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                
                elif (opcao == "2"):
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
                
                elif(opcao == "3"):
                    os.system("cls")
                    Menu.menuClienteAtualizar()
                    opcao = input("INFORME A OPÇÃO DESEJADA: ")
                    
                    if(opcao == "0"):
                        os.system("cls")
                        continue

                    elif(opcao == "1" or opcao == "2"):
                        cpf = input("INFORME O CPF DO CLIENTE: ")
                        cliente = ClienteDAO().getByCpf(cpf)
                        if(cliente == None):
                            MessageManager.customMessage("CLIENTE NÃO ENCONTRADO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                            os.system("cls")
                            continue
                        elif(opcao == "1"):
                            email = input("INFORME O NOVO E-MAIL DO CLIENTE: ")
                            ClienteDAO().update(id=cliente.id, novoEmail=email, novoCelular=None)
                            

                        elif(opcao == "2"):
                            celular = input("INFORME O NOVO CELULAR DO CLIENTE: ")
                            ClienteDAO().update(id=cliente.id, novoEmail=None, novoCelular=celular)

                        MessageManager.customMessage("CLIENTE ATUALIZADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)

                    else:
                        MessageManager.invalidOption()
                
                else:
                    MessageManager.invalidOption()
                
            elif(opcao == "2"):
                os.system("cls")
                Menu.menuVoo()
                opcao = input("INFORME A OPÇÃO DESEJADA: ")
                if(opcao == "0"):
                    os.system("cls")
                    continue                 
                
                elif(opcao == "1"):
                    print("============================")
                    origem = input("INFORME O LOCAL DE ORIGEM DO VOO: ")
                    destino = input("INFORME O LOCAL DE DESTINO DO VOO: ")
                    data = input("INFORME A DATA DO VOO(dd/mm/aaaa): ")

                    voo = Voo(id=None, origem=origem, destino=destino, data=data)
                    VooDAO().insert(voo)
                    MessageManager.customMessage("VOO CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)

                elif(opcao == "2"):
                    print("============================")
                    id = input("INFORME O ID DO VOO: ")
                    voo = VooDAO().getById(id)
                    if(voo != None):
                        table = PrettyTable()
                        table.field_names = ["ID", "LOCAL DE PARTIDA", "LOCAL DE DESTINO", "DATA"]
                        table.add_row([voo.id, voo.origem, voo.destino, voo.data])
                        print(table)
                        MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)
                    
                    else:
                        MessageManager.customMessage("VOO NÃO ENCONTRADO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

                elif(opcao == "3"):
                    print("============================")
                    id = input("INFORME O ID DO VOO: ")
                    if(VooDAO().delete(int(id))):
                        MessageManager.customMessage("VOO DELETADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)
                    else:
                        MessageManager.customMessage("HOUVE UM ERRO AO DELETAR O VOO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)


                else:
                    MessageManager.invalidOption()

                
            elif(opcao == "3"):
                os.system("cls")
                Menu.menuReserva()
                opcao = input("INFORME A OPÇÃO DESEJADA: ")
                if(opcao == "0"):
                    os.system("cls")
                    continue   

                elif(opcao == "1"):
                    print("============================")
                    cpfCliente = input("INFORME O CPF DO CLIENTE: ")
                    cliente = ClienteDAO().getByCpf(cpfCliente)
                    if (cliente == None):
                        MessageManager.customMessage("CLIENTE NÃO ENCONTRADO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                        os.system("cls")
                        continue
                    
                    idVoo = input("INFORME O ID DO VOO: ")
                    voo = VooDAO().getById(idVoo)
                    if(voo == None):
                        MessageManager.customMessage("VOO NÃO ENCONTRADO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                        os.system("cls")
                        continue

                    dataAtual = date.today().strftime("%d/%m/%Y")
                    try:
                        valor = float(input("INFORME O VALOR DA RESERVA: "))
                        reserva = Reserva(id = None, cliente = cliente.id, voo = voo.id, data=dataAtual, valor=valor)
                        ReservaDAO().insert(reserva=reserva)
                        MessageManager.customMessage("RESERVA CADASTRADA COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)
                    except ValueError:
                        MessageManager.customMessage("VALOR DA RESERVA INVÁLIDO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

                elif(opcao == "2"):
                    id = input("INFORME O ID DA RESERVA: ")
                    reserva = ReservaDAO().getById(id)
                    if(reserva != None):
                        cliente = ClienteDAO().getById(reserva.idCliente)
                        voo = VooDAO().getById(reserva.idVoo)
                        table = PrettyTable()
                        table.field_names = ["ID DA RESERVA", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
                        table.add_row([reserva.id, cliente.nome, cliente.cpf, cliente.email, voo.origem, voo.destino, voo.data, reserva.data, reserva.valor])
                        print(table)
                        MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)
                    else:
                        MessageManager.customMessage("RESERVA NÃO ENCONTRADA, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

                elif(opcao == "3"):
                    print("============================")
                    idVoo = input("INFORME O ID DO VOO: ")
                    voo = VooDAO().getById(int(idVoo))
                    if(voo == None):
                        MessageManager.customMessage("VOO NÃO ENCONTRADO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                        os.system("cls")
                        continue
                    
                    listaReservas = ReservaDAO().listByVooId(idVoo)
                    table = PrettyTable()
                    table.field_names = ["ID DA RESERVA", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
                    for reserva in listaReservas:
                        table.add_row([reserva.id, reserva.cliente.nome, reserva.cliente.cpf, reserva.cliente.email, reserva.voo.origem, reserva.voo.destino, reserva.voo.data, reserva.data, reserva.valor], divider=True)

                    print(table)
                    MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)
                else:
                    MessageManager.invalidOption()

            else:
                MessageManager.invalidOption()
            
            os.system("cls")
            
    
CompanhiaAerea.main()
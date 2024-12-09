import sys
import os
from datetime import date
from prettytable import PrettyTable
from controller.ClienteController import ClienteController
from utils.Menu import Menu
from utils.MessageManager import MessageManager
from model.dao.ClienteDAO import ClienteDAO
from model.dao.VooDAO import VooDAO
from model.dao.ReservaDAO import ReservaDAO
from model.entity.Reserva import Reserva
from service.VooService import VooService
from exceptions.InvalidPatternException import InvalidPatternException
from exceptions.RegisterNotFoundException import RegisterNotFoundException

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class CompanhiaAerea:

    clienteController = ClienteController()
    vooService = VooService()

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
                    CompanhiaAerea.clienteController.cadastrarCliente()
                
                elif (opcao == "2"):
                    CompanhiaAerea.clienteController.relatorioCliente()
                
                elif(opcao == "3"):
                    os.system("cls")
                    Menu.menuClienteAtualizar()
                    opcao = input("INFORME A OPÇÃO DESEJADA: ")
                    
                    if(opcao == "0"):
                        os.system("cls")
                        continue

                    elif(opcao == "1" or opcao == "2"):
                        CompanhiaAerea.clienteController.atualizarCliente(opcao)

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
                    try:
                        print("============================")
                        origem = input("INFORME O LOCAL DE ORIGEM DO VOO: ")
                        destino = input("INFORME O LOCAL DE DESTINO DO VOO: ")
                        data = input("INFORME A DATA DO VOO(dd/mm/aaaa): ")

                        CompanhiaAerea.vooService.cadastrarVoo(origem, destino, data)
                        MessageManager.customMessage("VOO CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)
                    
                    except InvalidPatternException as e:
                        MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

                elif(opcao == "2"):
                    print("============================")
                    id = input("INFORME O ID DO VOO: ")
                    try:
                        voo = VooDAO().getById(id)
                    
                        table = PrettyTable()
                        table.field_names = ["ID", "LOCAL DE PARTIDA", "LOCAL DE DESTINO", "DATA"]
                        table.add_row([voo.id, voo.origem, voo.destino, voo.data])
                        print(table)
                        MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)
                    
                    except RegisterNotFoundException as e:
                        MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

                elif(opcao == "3"):
                    print("============================")
                    id = input("INFORME O ID DO VOO: ")
                    try:
                        VooDAO().getById(id)
                        if(VooDAO().delete(int(id))):
                            MessageManager.customMessage("VOO DELETADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)
                        else:
                            MessageManager.customMessage("HOUVE UM ERRO AO DELETAR O VOO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                    except RegisterNotFoundException as e:
                        MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

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
                    idVoo = input("INFORME O ID DO VOO: ")
                    try:
                        cliente = ClienteDAO().getByCpf(cpfCliente)
                    
                        voo = VooDAO().getById(idVoo)

                        dataAtual = date.today().strftime("%d/%m/%Y")
                    
                        try:
                            valor = float(input("INFORME O VALOR DA RESERVA: "))
                            
                            reserva = Reserva(id = None, cliente = cliente.id, voo = voo.id, data=dataAtual, valor=valor)
                            ReservaDAO().insert(reserva=reserva)
                            MessageManager.customMessage("RESERVA CADASTRADA COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)
                        
                        except ValueError:
                            MessageManager.customMessage("VALOR DA RESERVA INVÁLIDO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                        
                    except RegisterNotFoundException as e:
                        MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                    
                    

                elif(opcao == "2"):
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

                elif(opcao == "3"):
                    print("============================")
                    idVoo = input("INFORME O ID DO VOO: ")
                    try:
                        voo = VooDAO().getById(int(idVoo))
                    
                        listaReservas = ReservaDAO().listByVooId(idVoo)
                        table = PrettyTable()
                        table.field_names = ["ID DA RESERVA", "NOME DO CLIENTE", "CPF DO CLIENTE", "E-MAIL DO CLIENTE", "ORIGEM DO VOO", "DESTINO DO VOO", "DATA DO VOO", "DATA DA RESERVA", "VALOR DA RESERVA"]
                        for reserva in listaReservas:
                            table.add_row([reserva.id, reserva.cliente.nome, reserva.cliente.cpf, reserva.cliente.email, reserva.voo.origem, reserva.voo.destino, reserva.voo.data, reserva.data, reserva.valor], divider=True)

                        print(table)
                        MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)
                    except RegisterNotFoundException as e:
                        MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
                
                else:
                    MessageManager.invalidOption()

            else:
                MessageManager.invalidOption()
            
            os.system("cls")
            
    
CompanhiaAerea.main()
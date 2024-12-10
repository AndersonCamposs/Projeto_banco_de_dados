import sys
import os
from controller import VooController
from controller.ClienteController import ClienteController
from controller.VooController import VooController
from controller.ReservaController import ReservaController
from utils.Menu import Menu
from utils.MessageManager import MessageManager

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class CompanhiaAerea:

    clienteController = ClienteController()
    vooController = VooController()
    reservaController = ReservaController()

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
                
                elif(opcao == "4"):
                    CompanhiaAerea.clienteController.listarClientes()
                
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
                    CompanhiaAerea.vooController.cadastraVoo()

                elif(opcao == "2"):
                    CompanhiaAerea.vooController.relatorioVoo()

                elif(opcao == "3"):
                    CompanhiaAerea.vooController.deletarVoo()

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
                    CompanhiaAerea.reservaController.cadastrarReserva()
                    
                elif(opcao == "2"):
                    CompanhiaAerea.reservaController.relatorioReserva()

                elif(opcao == "3"):
                    CompanhiaAerea.reservaController.listarReservasVoo()
                
                else:
                    MessageManager.invalidOption()

            else:
                MessageManager.invalidOption()
            
            os.system("cls")
            
CompanhiaAerea.main()
import sys
import os
from controller import VooController
from controller.ClienteController import ClienteController
from controller.VooController import VooController
from controller.ReservaController import ReservaController
from utils.Menu import Menu
from utils.MessageManager import MessageManager
from view.ClienteView import ClienteView

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class CompanhiaAerea:

    clienteView = ClienteController()
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
                clienteView = ClienteView()
                opcao = input("INFORME A OPÇÃO DESEJADA: ")
                
                if(opcao == "0"):
                    os.system("cls")
                    continue 
                
                elif (opcao == "1"):
                    clienteView.formularioInserir()
                
                elif (opcao == "2"):
                    clienteView.formularioRelatorio()
                
                elif(opcao == "3"):
                    os.system("cls")
                    clienteView.formularioAtualizar()
                
                elif(opcao == "4"):
                    clienteView.exibirTodos()
                
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

                elif(opcao == "4"):
                    CompanhiaAerea.vooController.listarVoos()

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
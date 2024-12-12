import sys
import os
from utils.Menu import Menu
from utils.MessageManager import MessageManager
from view.ReservaView import ReservaView
from view.VooView import VooView
from view.ClienteView import ClienteView

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class CompanhiaAerea:
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
                vooView = VooView()
                opcao = input("INFORME A OPÇÃO DESEJADA: ")
                if(opcao == "0"):
                    os.system("cls")
                    continue                 
                
                elif(opcao == "1"):
                    vooView.formularioInserir()

                elif(opcao == "2"):
                    vooView.formularioRelatorio()

                elif(opcao == "3"):
                    vooView.formularioDeletar()

                elif(opcao == "4"):
                    vooView.exibirTodos()

                else:
                    MessageManager.invalidOption()

                
            elif(opcao == "3"):
                os.system("cls")
                reservaView = ReservaView()
                opcao = input("INFORME A OPÇÃO DESEJADA: ")
                if(opcao == "0"):
                    os.system("cls")
                    continue   

                elif(opcao == "1"):
                    reservaView.formularioInserir()
                    
                elif(opcao == "2"):
                    reservaView.formularioRelatorio()

                elif(opcao == "3"):
                    reservaView.exibirTodosPorVoo()
                
                else:
                    MessageManager.invalidOption()

            else:
                MessageManager.invalidOption()
            
            os.system("cls")
            
CompanhiaAerea.main()
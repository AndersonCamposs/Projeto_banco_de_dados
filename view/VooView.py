from prettytable import PrettyTable
from controller.VooController import VooController
from exceptions.InvalidPatternException import InvalidPatternException
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from utils.Menu import Menu
from utils.MessageManager import MessageManager


class VooView:
    def __init__(self):
        self._vooControler = VooController()
        Menu.menuVoo()

    def formularioInserir(self):
        try:
            print("============================")
            origem = input("INFORME O LOCAL DE ORIGEM DO VOO: ")
            destino = input("INFORME O LOCAL DE DESTINO DO VOO: ")
            data = input("INFORME A DATA DO VOO(dd/mm/aaaa): ")
            
            cod = self._vooControler.cadastraVoo(origem, destino, data)
            MessageManager.customMessage(f"VOO DE CÓDIGO {cod} CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.SUCCESS)
        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def formularioRelatorio(self):
        print("============================")
        cod = input("INFORME O CÓDIGO DO VOO: ")
        try:
            voo = self._vooControler.relatorioVoo(cod)
        
            table = PrettyTable()
            table.field_names = ["CÓD.", "LOCAL DE PARTIDA", "LOCAL DE DESTINO", "DATA"]
            table.add_row([voo.cod, voo.origem, voo.destino, voo.data])
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def formularioDeletar(self):
        print("============================")
        cod = input("INFORME O CÓDIGO DO VOO: ")
        try:
            self._vooControler.deletarVoo(cod)
            MessageManager.customMessage(f"VOO DE CÓDIGO {cod} DELETADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def exibirTodos(self):
        try:
            listaVoos = self._vooControler.listarVoos()
            table = PrettyTable()
            table.field_names = ["CÓD.", "LOCAL DE PARTIDA", "LOCAL DE DESTINO", "DATA"]
            for voo in listaVoos:
                table.add_row([voo.cod, voo.origem, voo.destino, voo.data], divider=True)
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)

        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

        except TypeError as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)


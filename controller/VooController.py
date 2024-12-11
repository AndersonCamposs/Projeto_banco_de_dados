from prettytable import PrettyTable
from exceptions.InvalidPatternException import InvalidPatternException
from exceptions.RegisterNotFoundException import RegisterNotFoundException
from model.dao.VooDAO import VooDAO
from service.VooService import VooService
from utils.MessageManager import MessageManager


class VooController:
    def __init__(self):
        self._vooService = VooService()

    @property
    def vooService(self):
        return self._vooService
    
    def cadastraVoo(self):
        try:
            print("============================")
            cod = input("INFORME O CÓDIGO DO VOO: ")
            origem = input("INFORME O LOCAL DE ORIGEM DO VOO: ")
            destino = input("INFORME O LOCAL DE DESTINO DO VOO: ")
            data = input("INFORME A DATA DO VOO(dd/mm/aaaa): ")

            self.vooService.cadastrarVoo(cod, origem, destino, data)
            MessageManager.customMessage("VOO CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.SUCCESS)
    
        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def relatorioVoo(self):
        print("============================")
        cod = input("INFORME O CÓDIGO DO VOO: ")
        try:
            voo = self._vooService.buscarPorCod(cod)
        
            table = PrettyTable()
            table.field_names = ["ID", "CÓD.", "LOCAL DE PARTIDA", "LOCAL DE DESTINO", "DATA"]
            table.add_row([voo.id, voo.cod, voo.origem, voo.destino, voo.data])
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def deletarVoo(self):
        print("============================")
        cod = input("INFORME O CÓDIGO DO VOO: ")
        try:
            self._vooService.deletarVoo(cod)
            MessageManager.customMessage("VOO DELETADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

    def listarVoos(self):
        try:
            listaVoos = self._vooService.listarVoos()
            table = PrettyTable()
            table.field_names = ["ID", "CÓD.", "LOCAL DE PARTIDA", "LOCAL DE DESTINO", "DATA"]
            for voo in listaVoos:
                table.add_row([voo.id, voo.cod, voo.origem, voo.destino, voo.data])
            print(table)
            MessageManager.customMessage("PRESSIONE ENTER PARA CONTINUAR", MessageManager.INFO)

        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)

        except TypeError as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.DANGER)
                
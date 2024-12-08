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
            origem = input("INFORME O LOCAL DE ORIGEM DO VOO: ")
            destino = input("INFORME O LOCAL DE DESTINO DO VOO: ")
            data = input("INFORME A DATA DO VOO(dd/mm/aaaa): ")

            self.vooService.cadastrarVoo(origem, destino, data)
            MessageManager.customMessage("VOO CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.success)
    
        except InvalidPatternException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)

    def relatorioVoo(self):
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

    def deletarVoo(self):
        print("============================")
        id = input("INFORME O ID DO VOO: ")
        try:
            self._vooService.deletarVoo(id)
            MessageManager.customMessage("VOO DELETADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR", MessageManager.info)
        
        except RegisterNotFoundException as e:
            MessageManager.customMessage(f"{str(e)}, PRESSIONE ENTER PARA CONTINUAR", MessageManager.danger)
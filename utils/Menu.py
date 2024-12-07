from prettytable import PrettyTable

class Menu:
    @staticmethod
    def menuPrincipal():
        table = PrettyTable()
        table.field_names = ["COD.", "OPÇÃO"]
        table.add_row(["1", "MENU CLIENTES"], divider=True)
        table.add_row(["2", "MENU VOOS"], divider=True)
        table.add_row(["3", "MENU RESERVAS"], divider=True)
        table.add_row(["0", "SAIR"], divider=True)
        print(table)

    @staticmethod
    def menuCliente():
        table = PrettyTable()
        table.field_names = ["COD.", "OPÇÃO"]
        table.add_row(["1", "NOVO CLIENTE"], divider=True)
        table.add_row(["2", "RELATÓRIO DO CLIENTE"], divider=True)
        table.add_row(["0", "VOLTAR"], divider=True)
        print(table)

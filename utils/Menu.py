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
        table.add_row(["2", "RELATÓRIO DE CLIENTE"], divider=True)
        table.add_row(["3", "ATUALIZAR DADOS DO CLIENTE"], divider=True)
        table.add_row(["0", "VOLTAR"], divider=True)
        print(table)

    @staticmethod
    def menuClienteAtualizar():
        table = PrettyTable()
        table.field_names = ["COD.", "OPÇÃO"]
        table.add_row(["1", "ATUALIZAR E-MAIL DO CLIENTE"], divider=True)
        table.add_row(["2", "ATUALIZAR CELULAR DO CLIENTE"], divider=True)
        table.add_row(["0", "VOLTAR"], divider=True)
        print(table)

    @staticmethod
    def menuVoo():
        table = PrettyTable()
        table.field_names = ["COD.", "OPÇÃO"]
        table.add_row(["1", "NOVO VOO"], divider=True)
        table.add_row(["2", "RELATÓRIO DE VOO"], divider=True)
        table.add_row(["0", "VOLTAR"], divider=True)
        print(table)

    @staticmethod
    def menuReserva():
        table = PrettyTable()
        table.field_names = ["COD.", "OPÇÃO"]
        table.add_row(["1", "NOVA RESERVA"], divider=True)
        table.add_row(["2", "RELATÓRIO DE RESERVA"], divider=True)
        table.add_row(["3", "BUSCAR RESERVAS POR VOO"], divider=True)
        table.add_row(["0", "VOLTAR"], divider=True)
        print(table)

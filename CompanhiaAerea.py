import sys
import os
from prettytable import PrettyTable
from utils.Menu import Menu
from model.dao.ClienteDAO import ClienteDAO
from model.entity.Cliente import Cliente

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
                Menu.menuCliente()
                opcao = input("INFORME A OPÇÃO DESEJADA: ")
                if (opcao == "1"):
                    print("============================")
                    nome = input("INFORME O NOME DO CLIENTE: ")
                    cpf = input("INFORME O CPF DO CLIENTE: ")
                    dataNascimento = input("INFORME A DATA DE NASCIMENTO(dd/mm/aaaa): ")
                    email = input("INFORME O EMAIL DO CLIENTE: ")
                    celular = input("INFORME O CELULAR DO CLIENTE: ")

                    cliente = Cliente(id=None, nome=nome, cpf=cpf, dataNascimento=dataNascimento, email=email, celular=celular)
                    ClienteDAO().insert(cliente)
                    print("+================================================================+")
                    print("| CLIENTE CADASTRADO COM SUCESSO, PRESSIONE ENTER PARA CONTINUAR |")
                    print("+================================================================+")
                    input()
                
                elif (opcao == "2"):
                    print("============================")
                    cpf = input("INFORME O CPF DO CLIENTE: ")
                    cliente = ClienteDAO().fetchByCpf(cpf)
                    table = PrettyTable()
                    table.field_names = ["ID", "NOME", "CPF", "DATA DE NASCIMENTO", "E-MAIL", "CELULAR"]
                    table.add_row([cliente.id, cliente.nome, cliente.cpf, cliente.dataNascimento, cliente.email, cliente.celular])
                    print(table)
                    print("+==========================================================================+")
                    print("|                       PRESSIONE ENTER PARA CONTINUAR                     |")
                    print("+==========================================================================+")
                    input()
                else:
                    print(
                        '''
        ++================================================================++
        || OPÇÃO INVÁLIDA, TENTE NOVAMENTE, PRESSIONE ENTER PARA CONTINUAR ||
        ++================================================================++
        '''
                    )
                    input()
                

            else:
                print(
                    '''
    ++================================================================++
    || OPÇÃO INVÁLIDA, TENTE NOVAMENTE, PRESSIONE ENTER PARA CONTINUAR ||
    ++================================================================++
    '''
                )
                input()
            
            os.system("cls")
            
    



CompanhiaAerea.main()
from typing import Union
from model.dao.ClienteDAO import ClienteDAO
from model.entity.Cliente import Cliente
from utils.Validator import Validator
from exceptions.RegisterNotFoundException import RegisterNotFoundException

class ClienteService():
    def __init__(self):
        pass

    
    def cadastrarCliente(self, nome: str, cpf: str, dataNascimento: str, email: str, celular: str) -> None:
        Validator.cpfValidation(cpf)
        Validator.dateValidation(dataNascimento)
        Validator.emailValidation(email)

        with ClienteDAO() as clienteDAO:
            clienteDAO.insert(Cliente(None, nome, cpf, dataNascimento, email, celular))

    def atualizarCliente(self, id: int, email: Union[str, None], celular: Union[str, None]):
        if(email):
            Validator.emailValidation(email)
        with ClienteDAO() as clienteDAO:
            clienteDAO.update(id, email, celular)

    def buscarPorCpf(self, cpf: str):
        with ClienteDAO() as clienteDAO:
            return clienteDAO.getByCpf(cpf)

    def buscarPorId(self, id: int):
        with ClienteDAO() as clienteDAO:
            return clienteDAO.clienteDAO.getById(id)
        
    def listarClientes(self):
        with ClienteDAO() as clienteDAO:
            return clienteDAO.listaAll()

        
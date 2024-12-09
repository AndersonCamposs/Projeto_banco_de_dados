from typing import Union
from model.dao.ClienteDAO import ClienteDAO
from model.entity.Cliente import Cliente
from utils.Validator import Validator
from exceptions.RegisterNotFoundException import RegisterNotFoundException

class ClienteService():
    def __init__(self):
        self._clienteDAO = ClienteDAO()

    @property
    def clienteDAO(self) -> ClienteDAO:
        return self._clienteDAO
    
    def cadastrarCliente(self, nome: str, cpf: str, dataNascimento: str, email: str, celular: str) -> None:
        Validator.cpfValidation(cpf)
        Validator.dateValidation(dataNascimento)
        Validator.emailValidation(email)

        self._clienteDAO.insert(Cliente(None, nome, cpf, dataNascimento, email, celular))

    def atualizarCliente(self, id: int, email: Union[str, None], celular: Union[str, None]):
        if(email):
            Validator.emailValidation(email)
        
from typing import Union
from model.entity import Cliente
from service.ClienteService import ClienteService
from utils.Validator import Validator


class ClienteController:
    def __init__(self):
        self._clienteService = ClienteService()

    @property
    def clienteService(self):
        return self._clienteService
    
    def cadastrarCliente(self, nome: str, cpf: str, dataNascimento: str, email: str, celular: str):
        Validator.cpfValidation(cpf)
        Validator.dateValidation(dataNascimento)
        Validator.emailValidation(email)
        self._clienteService.cadastrarCliente(nome, cpf, dataNascimento, email, celular)
            
    def relatorioCliente(self, cpf) -> Cliente:    
        return self._clienteService.buscarPorCpf(cpf)
            
    def atualizarCliente(self, cpf: str, email: Union[str, None], celular: Union[str, None]):
        Validator.cpfValidation(cpf)
        
        cliente = self._clienteService.buscarPorCpf(cpf)
        if(email):
            self._clienteService.atualizarCliente(cliente.id, email, None)
        elif(celular):
            self._clienteService.atualizarCliente(cliente.id, None, celular)         
        
    def listarClientes(self):
        return self._clienteService.listarClientes()
            
        
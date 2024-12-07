from typing import Union

class Cliente:
    def __init__(self, id: Union[int, None], nome: str, cpf:str, dataNascimento: str, email: str, celular: str) -> None:
        # ATRIBUTOS PRIVADOS
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._dataNascimento = dataNascimento
        self._email = email
        self._celular = celular

    @property
    def id(self) -> int:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def dataNascimento(self) -> str:
        return self._dataNascimento
    
    @property 
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, novoEmail: str) -> None:
        self._email = novoEmail

    @property
    def celular(self) -> str:
        return self._celular
    @celular.setter
    def celular(self, novoCelular: str) -> None:
        self._celular = novoCelular


    

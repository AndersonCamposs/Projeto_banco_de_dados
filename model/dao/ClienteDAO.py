from model.dao.GenericDAO import GenericDAO
from model.entity.Cliente import Cliente

class ClienteDAO(GenericDAO):
    def __init__(self):
        super().__init__()

    def insert(self, cliente : Cliente) -> None:
        self.cursor.execute(
            '''INSERT INTO Cliente (nome, cpf, data_nascimento, email, celular)
            VALUES (?, ?, ?, ?, ?)''',
            [cliente.nome, cliente.cpf, cliente.dataNascimento, cliente.email, cliente.celular]
        )
        self.conn.commit()
        
    
    def fetchByCpf(self, cpf: str) -> Cliente: 
        self.cursor.execute(
            '''SELECT * FROM Cliente WHERE cpf = ?''',
            [cpf]
        )
        data = self.cursor.fetchone()
        
        try:
            cliente = Cliente(id=data[0], nome=data[1], cpf=data[2], 
            dataNascimento=data[3], email=data[4], celular=data[5])
        except TypeError:
            return None
        
        return cliente
    

    
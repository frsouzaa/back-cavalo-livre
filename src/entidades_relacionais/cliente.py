from datetime import datetime


class Cliente:
    id: int
    nome: str
    sobrenome: str
    email: str
    senha: str
    nascimento: datetime
    pais: str
    sexo: str


    def __init__(self, id: int, nome: str, sobrenome: str, email: str, senha: str, nascimento: datetime, pais: str, sexo: str):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.nascimento = nascimento
        self.pais = pais
        self.sexo = sexo

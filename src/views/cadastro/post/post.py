from ....decorators.validar_request import Validar_Request
from flask import request
from ....banco.banco import Banco
from datetime import datetime
import bcrypt


class Post():
    banco: Banco


    def __init__(self) -> None:
        self.banco = Banco()


    @Validar_Request({
        'data': {
            'type': 'dict',
            'empty': False, 
            'required': True,
            'schema': {
                'email': {'type': 'string', 'empty': False, 'required': True},
                'senha': {'type': 'string', 'empty': False, 'required': True},
                'nome': {'type': 'string', 'empty': False, 'required': True},
                'sobrenome': {'type': 'string', 'empty': False, 'required': True},
                'pais': {'type': 'string', 'empty': False, 'required': True},
                'nascimento': {'type': 'string', 'empty': False, 'required': True},
                'sexo': {'type': 'string', 'empty': False, 'required': True},
                'cpf': {'type': 'string', 'empty': False, 'required': True},
            },
        }
    })
    def handle_request(self):
        try:
            req_json = request.get_json().get("data")

            self.banco.conectar() == True
            
            nascimento = datetime.strptime(req_json.get("nascimento"), "%d/%m/%Y")
            query = f"""
                INSERT INTO cliente(
                    nome, sobrenome,
                    email, senha,
                    pais, sexo,
                    nascimento, cpf
                ) 
                values(
                    "{req_json.get("nome")}", "{req_json.get("sobrenome")}",
                    "{req_json.get("email")}", "{self.criptografar_senha(req_json.get("senha"))}",
                    "{req_json.get("pais")}", "{req_json.get("sexo")}",
                    "{nascimento.strftime("%Y-%m-%d")}", "{req_json.get("cpf")}"
                );
            """
            self.banco.execultar(query)

            self.banco.desconectar()
            return {"msg": "ok"}, 200
        except Exception as e:
            return {"msg": "erro"}, 500


    def criptografar_senha(self, senha: str) -> str:
        salt = bcrypt.gensalt()
        hash_senha = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return hash_senha.decode('utf-8')
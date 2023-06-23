from ....decorators.validar_request import Validar_Request
from flask import request
from ....banco.banco import Banco
from ....utils.jwt import JWT
from ....utils.senha import Senha
import random
import string


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
                'senha': {'type': 'string', 'empty': False, 'required': False},
                'senhaC': {'type': 'string', 'empty': False, 'required': False}
            },
        }
    })
    def handle_request(self):
        try:
            req_json = request.get_json().get("data")
                
            self.banco.conectar() == True
            
            query = f"""
                select * from cliente where email = "{req_json.get("email")}"
            """
            res = self.banco.execultar(query)[0]

            if not res:
                return {"msg": "login ou senha inválidos"}, 404
            
            res = res[0]
            
            if req_json.get("senha") and not Senha.descriptografar(req_json.get("senha"), res.get("senha")):
                return {"msg": "login ou senha inválidos"}, 404
            elif req_json.get("senhaC") and res.get("senha") != req_json.get("senhaC"):
                return {"msg": "login ou senha inválidos"}, 404
            
            if req_json.get("senhaC"):
                req_json["senhaC"] = self.gerar_senha()
            token = JWT().gerar(req_json)

            query = f"""
                insert into sessao(id_cliente, token) values({res.get("id")}, "{token}")
            """
            self.banco.execultar(query)

            self.banco.desconectar()
            return {
                "data": {
                    "token": token,
                    "email": res["email"],
                    "nome": res["nome"],
                    "sobrenome": res["sobrenome"],
                    "nascimento": res["nascimento"],
                    "pais": res["pais"],
                    "sexo": res["sexo"],
                    "cpf": res["cpf"],
                    "senha": res["senha"]
                }
            }, 200
        except Exception as e:
            return {"msg": "Erro"}, 500


    def gerar_senha(self) -> str:
        characters = string.ascii_letters + string.digits
        while True:
            password = ''.join(random.choice(characters) for _ in range(15))
            if any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
                return password

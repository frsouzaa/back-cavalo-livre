from ....decorators.validar_request import Validar_Request
from flask import request
from ....banco.banco import Banco
import bcrypt
from ....entidades_relacionais.cliente import Cliente
import jwt
from typing import Dict
from os import getenv
from datetime import datetime, timedelta


class Post():


    def __init__(self) -> None:
        self.banco = Banco()

    

    @Validar_Request({
        'data': {
            'type': 'dict',
            'schema': {
                'email': {'type': 'string', 'empty': False, 'required': True},
                'senha': {'type': 'string', 'empty': False, 'required': True}
            },
            'required': True
        }
    })
    def handle_request(self):
        try:
            req_json = request.get_json().get("data")
                
            self.banco.conectar() == True
            
            query = f"""
                select * from cliente where email = "{req_json.get("email")}"
            """
            res = self.banco.execultar(query)

            if not res:
                return {"menssagem": "login ou senha inválidos"}, 404
            
            res = res[0]
            cliente = Cliente(id=res[0],
                              nome=res[1],
                              sobrenome=res[2],
                              email=res[3],
                              senha=res[4],
                              nascimento=res[5],
                              pais=res[6], 
                              sexo=res[7])
            
            if not self.descriptografar_senha(req_json.get("senha"), cliente.senha):
                return {"menssagem": "login ou senha inválidos"}, 404

            token = self.gerar_token_jwt(req_json)

            query = f"""
                insert into sessao(id_cliente, token) values({cliente.id}, "{token}")
            """
            self.banco.execultar(query)

            self.banco.desconectar()
            return {"token": token}, 200
        except Exception as e:
            return {"menssagem": "erro"}, 500
    

    def descriptografar_senha(self, senha: str, hash_senha: str):
        return bcrypt.checkpw(senha.encode('utf-8'), hash_senha.encode('utf-8'))


    def gerar_token_jwt(self, payload: Dict[str, any]) -> str:
        validade = datetime.utcnow() + timedelta(seconds=30)
        payload['exp'] = validade
        token = jwt.encode(payload, getenv("key"), 'HS256')
        return token
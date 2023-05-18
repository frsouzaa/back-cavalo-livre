from ....decorators.validar_request import Validar_Request
from typing import Dict
from flask import request
from ....banco.banco import Banco
from datetime import datetime


class Post():
    banco: Banco


    def __init__(self) -> None:
        self.banco = Banco()


    @Validar_Request({
        'data': {
            'type': 'dict',
            'schema': {
                'email': {'type': 'string', 'empty': False, 'required': True},
                'senha': {'type': 'string', 'empty': False, 'required': True},
                'nome': {'type': 'string', 'empty': False, 'required': True},
                'sobrenome': {'type': 'string', 'empty': False, 'required': True},
                'pais': {'type': 'string', 'empty': False, 'required': True},
                'nascimento': {'type': 'string', 'empty': False, 'required': True},
                'sexo': {'type': 'string', 'empty': False, 'required': True},
            },
            'required': True
        }
    })
    def handle_request(self):
        try:
            assert self.banco.conectar() == True
        except Exception as e:
            return {"menssagem": "erro"}, 500
            
        req_json: Dict[str, any] = request.get_json().get("data")
        conexao = self.banco.get_conexao()

        try:
            assert conexao
        except Exception as e:
            return {"menssagem": "erro"}, 500
        

        nascimento = datetime.strptime(req_json.get("nascimento"), "%d/%m/%Y")
        query = f"""
            INSERT INTO cliente(
                nome, sobrenome,
                email, senha,
                pais, sexo,
                nascimento
            ) 
            values(
                "{req_json.get("nome")}", "{req_json.get("sobrenome")}",
                "{req_json.get("email")}", "{req_json.get("senha")}",
                "{req_json.get("pais")}", "{req_json.get("sexo")}",
                "{nascimento.strftime("%Y-%m-%d")}"
            );
        """
        res = self.banco.execultar(query)

        try:
            assert self.banco.desconectar() == True
        except Exception as e:
            return {"menssagem": "erro"}, 500
        
        return {"menssagem": "ok"}, 200


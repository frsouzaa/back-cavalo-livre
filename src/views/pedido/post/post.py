from ....decorators.validar_request import Validar_Request
from flask import request
from ....banco.banco import Banco
from typing import Tuple, Dict
from os import getenv
from datetime import datetime, timedelta


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
                'usuario': {'type': 'string', 'empty': False, 'required': True},
                'produtos': {
                    'type': 'list', 
                    'empty': False, 
                    'required': True
                }
            },
        }
    })
    def handle_request(self) -> Tuple[Dict[str, any], int]:
        try:
            req_json = request.get_json().get("data")
                
            self.banco.conectar() == True

            query = f"""
                select * from cliente where email = "{req_json.get("usuario")}"
            """
            usuario = self.banco.execultar(query)[0]

            if not usuario:
                return {"msg": "Erro"}, 404
            usuario = usuario[0]

            lista_prod = [str(i["id"]) for i in req_json.get("produtos")]

            query = f"""
                select id, preco from produto where id in ({','.join(lista_prod)})
            """
            precos = self.banco.execultar(query)[0]
            precos = {i.get("id"): i.get("preco") for i in precos}

            query = f"""
                insert into pedido(id_cliente) values({usuario.get("id")})
            """
            id_pedido = self.banco.execultar(query)[1]

            values = [
                f"""(
                        {i.get("quantidade")}, 
                        {precos.get(i.get("id"))},
                        {id_pedido},
                        {i.get("id")}
                    )""" for i in req_json.get("produtos")
            ]

            query = f"""
                insert into item(quantidade, valor_unitario, id_pedido, id_produto) 
                values {",".join(values)};
            """

            self.banco.execultar(query)

            self.banco.desconectar()
            return {"msg": "Sucesso"}, 200
        except Exception as e:
            return {"msg": "Erro"}, 500

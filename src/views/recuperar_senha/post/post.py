from ....decorators.validar_request import Validar_Request
from flask import request
from ....banco.banco import Banco
from typing import Tuple, Dict
import random
import string
from ....utils.email import Email
from ....utils.senha import Senha


class Post():
    banco: Banco
    email: Email


    def __init__(self) -> None:
        self.banco = Banco()
        self.email = Email()


    @Validar_Request({
        'data': {
            'type': 'dict',
            'empty': False, 
            'required': True,
            'schema': {
                'usuario': {'type': 'string', 'empty': False, 'required': True},
            },
        }
    })
    def handle_request(self) -> Tuple[Dict[str, any], int]:
        try:
            req_json = request.get_json().get("data")
            email = req_json.get("usuario")
                
            self.banco.conectar()

            query = f"""
                select * from cliente where email = "{email}"
            """
            usuario = self.banco.execultar(query)[0]

            if not usuario:
                return {"msg": "Se o cadastro existir uma senha será envia no e-mail informado."}, 200
            
            senha = self.gerar_senha()

            query = f"""
                update cliente set senha="{Senha.criptografar(senha)}" where email = "{email}"
            """
            res = self.banco.execultar(query)

            self.email.enviar(
                email,
                "E-mail de recuperação de senha.",
                f"Sua nova senha é: {senha}"
            )

            self.banco.desconectar()
            return {"msg": "Se o cadastro existir uma senha será envia no e-mail informado."}, 200
        except Exception as e:
            return {"msg": "Erro"}, 500
        
    

    def gerar_senha(self) -> str:
        characters = string.ascii_letters + string.digits
        while True:
            password = ''.join(random.choice(characters) for _ in range(15))
            if any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
                return password

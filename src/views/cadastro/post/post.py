from ....decorators.validar_request import Validar_Request


class Post():
    

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
        return {"menssagem": "ok"}, 200


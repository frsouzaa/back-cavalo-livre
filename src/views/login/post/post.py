from ....decorators.validar_request import Validar_Request


class Post():
    

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
        return {"menssagem": "ok"}, 200
    

    def valida_usuario(self):
        ...

from ....decorators.validar_token import Validar_Token


class Post():
    

    @Validar_Token
    def handle_request():
        return {"data": "Produtos"}, 200

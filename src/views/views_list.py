from typing import List


class View_List():
    list: List


    def __init__(self) -> None:
        self.list = [
            Produtos,
            Login,
            Cadastro,
            Pedido,
            Recuperar_Senha
        ]


from .produtos.view import Produtos
from .login.view import Login
from .cadastro.view import Cadastro
from .pedido.view import Pedido
from .recuperar_senha.view import Recuperar_Senha

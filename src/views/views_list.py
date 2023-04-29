from typing import List


class View_List():
    list: List


    def __init__(self) -> None:
        self.list = [
            Produtos,
            Login
        ]


from .produtos.view import Produtos
from .login.view import Login
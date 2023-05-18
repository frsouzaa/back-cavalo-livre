

class Pedido():
    id: int
    id_produto: int
    id_categoria: int


    def __init__(self, id: int, id_produto: int, id_categoria: int) -> None:
        self.id = id
        self.id_produto = id_produto
        self.id_categoria = id_categoria
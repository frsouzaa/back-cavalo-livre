

class Item():
    id: int
    quantidade: int
    valor_unitario: float
    id_pedido: int
    id_produto: int


    def __init__(self, id: int, quantidade: int, valor_unitario: float, id_pedido: int, id_produto: int) -> None:
        self.id = id
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.id_pedido = id_pedido
        self.id_produto = id_produto

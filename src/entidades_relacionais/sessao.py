

class Produto():
    id: int
    token: str
    id_cliente: int


    def __init__(self, id: int, token: str, id_cliente: float) -> None:
        self.id = id
        self.token = token
        self.id_cliente = id_cliente

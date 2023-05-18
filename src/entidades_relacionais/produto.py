

class Produto():
    id: int
    nome: str
    preco: float
    descricao: str
    imagens: str


    def __init__(self, id: int, nome: str, preco: float, descricao: str, imagens: str) -> None:
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.imagens = imagens

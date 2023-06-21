from ....banco.banco import Banco


class Get():
    banco: Banco


    def __init__(self) -> None:
        self.banco = Banco()
    

    def handle_request(self):
        try:
            self.banco.conectar() == True
            
            query = f"""
                select p.id, p.nome, p.preco, p.imagens, p.descricao, group_concat(c.nome ) as categorias from categoria c
                inner join produto_x_categoria pc on pc.id_categoria = c.id
                inner join produto p on p.id = pc.id_produto
                group by p.id
                ;
            """
            res = self.banco.execultar(query)

            for i in range(len(res)):
                res[i]["imagens"] = res[i]["imagens"].split("|")
                res[i]["categorias"] = res[i]["categorias"].split(",")

            self.banco.desconectar()
            return {"data": res}, 200
        except Exception as e:
            return {"msg": "erro"}, 500

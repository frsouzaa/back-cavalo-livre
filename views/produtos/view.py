from flask.views import View as FlaskView
from flask import request, Response
from typing import List


class Produtos(FlaskView):
    rota: str = '/produtos'
    methods: List[str] = ['GET']
    name: str = __name__

    
    def dispatch_request(self) -> Response:
        print("Produtos")
        return {"data": "Produtos"}, 200
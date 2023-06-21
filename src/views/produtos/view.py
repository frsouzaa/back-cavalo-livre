from flask.views import View as FlaskView
from flask import Response
from typing import List
from .get.get import Get


class Produtos(FlaskView):
    rota: str = '/produtos'
    methods: List[str] = ['GET']
    name: str = __name__

    
    def dispatch_request(self) -> Response:
        return self.post()


    def post(self):
        return Get().handle_request()

from flask.views import View as FlaskView
from flask import Response
from typing import List
from .post.Post import Post


class Produtos(FlaskView):
    rota: str = '/produtos'
    methods: List[str] = ['POST']
    name: str = __name__

    
    def dispatch_request(self) -> Response:
        return self.post()


    def post(self):
        return Post().handle_request()

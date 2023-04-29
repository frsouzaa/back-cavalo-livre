from typing import Callable, Dict
from flask import request
from cerberus import Validator


class Validar_Request():
    req: Dict[str,any]
    func: Callable


    def __init__(self, req=None):
        self.req = req


    def __call__(self, func:Callable, *args, **kwargs):
        def valida_request(f=None):
            conteudoRequest = {
                'json': request.get_json(),
                'args': request.args
            }
            v = Validator(self.req)
            if (v.validate(conteudoRequest["json"]) is not True):
                return {"menssagem": v.errors}, 400
            if f is not None:
                return func(f, *args, **kwargs)
            return func(*args,**kwargs)
        return valida_request

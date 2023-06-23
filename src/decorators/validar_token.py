import jwt
from flask import request, jsonify
from typing import Callable
from os import getenv


class Validar_Token():


    def __init__(self, func: Callable)-> None:
        self.func = func


    def __call__(self, *args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            return jsonify({'msg': 'Está faltando o token'}), 401
        try:
            jwt.decode(token, getenv("key"), algorithms=["HS256"])
        except:
            return jsonify({'msg': 'Token inválido'}), 401
        return self.func(*args, **kwargs)
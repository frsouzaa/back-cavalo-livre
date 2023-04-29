import jwt
from flask import request, jsonify
from typing import Callable


class Validar_Token():


    def __init__(self, func:Callable)-> None:
        self.func = func


    def __call__(self, *args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            return jsonify({'mensagem': 'Está faltando o token'}), 401
        try:
            data = jwt.decode(token, 'your-secret-key', algorithms=["HS256"])
        except:
            return jsonify({'mensagem': 'Token inválido'}), 401
        return self.func(*args, **kwargs)

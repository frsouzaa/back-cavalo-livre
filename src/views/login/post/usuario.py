from flask import request


class Usuario:
    email: str
    senha: str


    def __init__(self) -> None:
        self.email = request.get_json().get('email')
        print(self.email)
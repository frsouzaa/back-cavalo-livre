from datetime import datetime, timedelta
from os import getenv
import jwt
from typing import Dict


class JWT():
    key: str
    validade: int


    def __init__(self) -> None:
        self.key = getenv("KEY")
        self.validade = int(getenv("SEGUNDOSJWT"))


    def gerar(self, payload: Dict[str, any]) -> str:
        validade = datetime.utcnow() + timedelta(seconds=self.validade)
        payload['exp'] = validade
        token = jwt.encode(payload, self.key, 'HS256')
        return token

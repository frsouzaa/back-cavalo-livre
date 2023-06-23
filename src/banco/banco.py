import mysql
from mysql.connector import MySQLConnection
from os import getenv
from typing import List, Tuple


class Banco():
    conexao: MySQLConnection
    

    def conectar(self) -> None:
        self.conexao = mysql.connector.connect(
            host=getenv("DB_HOST"), database=getenv("DB"), user=getenv("DB_USUARIO"), password=getenv("DB_SENHA")
        )


    def get_conexao(self) -> MySQLConnection | None:
        if not self.conexao: return
        return self.conexao


    def execultar(self, comando: str) -> Tuple[List[dict], int]:
        cursor = self.conexao.cursor(dictionary=True)
        cursor.execute(comando)
        ultimo_id = cursor.lastrowid
        res = cursor.fetchall()
        self.conexao.commit()
        return res, ultimo_id
            
    
    def desconectar(self) -> None:
        self.conexao.close()
        
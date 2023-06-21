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


    def execultar(self, comando: str) -> List[Tuple]:
        cursor = self.conexao.cursor(dictionary=True)
        cursor.execute(comando)
        res = cursor.fetchall()
        self.conexao.commit()
        return res
            
    
    def desconectar(self) -> None:
        self.conexao.close()
        
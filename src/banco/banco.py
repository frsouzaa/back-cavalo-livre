import mysql
from mysql.connector import MySQLConnection
from os import getenv


class Banco():
    conexao: MySQLConnection
    

    def conectar(self) -> bool:
        try:
            self.conexao = mysql.connector.connect(
                host=getenv("DB_HOST"), database=getenv("DB"), user=getenv("DB_USUARIO"), password=getenv("DB_SENHA")
            )
            return True
        except Exception as e:
            return False
    

    def get_conexao(self) -> MySQLConnection | bool:
        if not self.conexao: return False
        return self.conexao


    def execultar(self, comando: str):
        cursor = self.conexao.cursor()
        cursor.execute(comando)
        res = cursor.fetchall()
        self.conexao.commit()
        return res
            
    
    def desconectar(self) -> bool:
        try:
            self.conexao.close()
            return True
        except Exception as e:
            return False
        
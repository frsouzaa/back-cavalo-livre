import smtplib
from email.message import EmailMessage
from os import getenv


class Email():
    email_cavalo: str
    senha_cavalo: str


    def __init__(self) -> None:
        self.email_cavalo = getenv("EMAIL")
        self.senha_cavalo = getenv("SENHA")


    def enviar(self, email: str, assunto: str, conteudo: str,) -> None:
        try:
            msg = EmailMessage()
            msg['Subject'] = assunto
            msg['From'] = self.email_cavalo
            msg['To'] = email
            msg.set_content(conteudo)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_cavalo, self.senha_cavalo)
                smtp.send_message(msg)
            return True
        except Exception as e:
            return False
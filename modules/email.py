import os
import smtplib
from typing import Sequence
from logging import info,error
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email_gmail(credential: dict, destiny: str | Sequence[str], subject: str, msg: str = None, file_path: str = None):
    '''
    '''
    try:
        info("Estabelecendo uma conexão com o servidor de email")
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            info("Habilitando a comunicação com o servidor de email")
            server.starttls()

            info("Autenticando no servidor de email")
            server.login(credential.get('email'), credential.get('password'))

            # Construir a mensagem de e-mail
            email_message = MIMEMultipart()
            email_message['From'] = credential.get("email")
            email_message['To'] = destiny
            email_message['Subject'] = subject

            if msg:
                email_message.attach(MIMEText(msg, 'html'))

            if file_path:
                with open(file_path, "rb") as attachment:
                    part = MIMEApplication(attachment.read(), Name=file_path)
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                email_message.attach(part)

            info("Enviando o email")
            server.sendmail(from_addr=credential.get("email"), to_addrs=destiny, msg=email_message.as_string())

            info("Encerrando conexão com o servidor de email")
    except Exception as ex:
        error(f"Erro no envio do email: {ex}")
        raise ex
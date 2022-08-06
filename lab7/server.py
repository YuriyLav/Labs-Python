import socket
# coding=utf-8
from smtplib import SMTP
import os
from dotenv import load_dotenv
from validate_email import validate_email

dotenv_path = '.env'
load_dotenv(dotenv_path)
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")
sender = 'sender.pyth@gmail.com'
password = 'sender.pyth191102'

HOST = '127.0.0.1'
PORT = 50007
HOST_COLLECTOR = '127.0.0.1'
PORT_COLLECTOR = 50008


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # связывает объект сокета с адресом
    s.listen(1)   # ожидание входящих запросов на соединение от клиентов
    conn, addr = s.accept()  # принимается входящее соединение, создается сокет, соответствующий новому соединению.
    # Сокет, для которого был вызван accept, остается в состоянии listen и готов к принятию следующих соединений.
    # Метод accept возвращает пару – socket-объект и адрес удаленного компьютера
    with conn:
        print('Connected by', addr)
        while True:
            email = conn.recv(1024).decode()  # чтение данных клиента
            mesg = conn.recv(2048).decode()
            valid = validate_email(email)  # проверка на корректность почты
            if not valid:
                conn.sendall(b'Mail is incorrect, please try again!')  # отправка данных клиенту
            else:
                ID = str(hash(email)) + str(hash(mesg))
                with SMTP(SMTP_HOST, SMTP_PORT) as smtp:
                    smtp.starttls()  # Переводит соединение с SMTP-сервером в режим TLS.
                    smtp.login(sender, password)
                    info = "\r\n".join(("From: %s" % sender, "To: %s" % sender, "Subject: %s" % ID, "", mesg))
                    smtp.sendmail(sender, sender, info)
                    info = "\r\n".join(("From: %s" % sender, "To: %s" % email, "Subject: %s" % ID, ""))
                    smtp.sendmail(sender, email, info)
                    conn.sendall(b'OK')
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
                        c.connect((HOST_COLLECTOR, PORT_COLLECTOR))  # подключаемся к коллектору
                        c.sendall(bytes(ID, 'utf-8'))
                conn, addr = s.accept()

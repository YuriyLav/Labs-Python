import socket
# coding=utf-8
HOST = '127.0.0.1'
PORT = 50007
# receiver.pyth@gmail.com
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # открытие сокета
    s.connect((HOST, PORT))  # подключаемся к серверу
    while True:
        email = bytes(input("Enter mail: "), 'utf-8')
        mesg = bytes(input("Enter message: "), 'utf-8')
        s.sendall(email)  # отправка данных серверу
        s.sendall(mesg)
        answer = (s.recv(1024)).decode()  # получение данных от сервера
        if answer != "OK":
            print(answer + "\n")
        else:
            break

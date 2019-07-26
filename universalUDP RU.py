import socket
from time import sleep
from threading import Thread

UDP_PORT = None
UDP_IP = None


class Server(Thread):
    def __init__(self, port):
        Thread.__init__(self)

        self.on = 1
        self.port = port

        self.serverSock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.bind(('', int(port)))

    def stop(self):
        self.on = 0
        self.serverSock.close()
        del self.serverSock

    def setPort(self, port):
        self.port = port

    def run(self):
        """Запуск потока"""
        while self.on == 1:
            try:
                data = self.serverSock.recv(1024)
                if not data:
                    break
                if self.on == 1:
                    print(data)
            except WindowsError:
                pass


print("Универсальный UDP клиент/сервер на Python")
print("Создан Neisvestney")
print("Краткая справка:\nРежимы работы: 1 - клиент, 2 - сервер, 3 - клиент/сервер\nВыход из режима - ctrl + c\nСмена ip - !chip, порта - !chport")
while True:
    mode = input("Режим или комманда:")
    if mode == "1":
        while True:
            try:
                if UDP_PORT == None or UDP_IP == None:
                    UDP_IP = input("Введите ip: ")
                    UDP_PORT = input("Введите порт: ")

                    clientSock = socket.socket(
                        socket.AF_INET, socket.SOCK_DGRAM)
                    clientSock.connect((UDP_IP, int(UDP_PORT)))

                inp = input("")

                clientSock.send(str.encode(inp))
                print("Отпраленно!")

            except KeyboardInterrupt:
                print("Выход из режима")
                break
    elif mode == "2":
        while True:
            try:
                if UDP_PORT == None:
                    UDP_PORT = input("Введите порт: ")

                server = Server(UDP_PORT)
                server.start()

                input("")

            except KeyboardInterrupt:
                server.stop()
                print("Выход из режима")
                break

    if mode == "3":
        if UDP_PORT == None:
            UDP_PORT = input("Введите порт: ")
        server = Server(UDP_PORT)
        server.start()
        while True:
            try:
                if UDP_IP == None:
                    UDP_IP = input("Введите ip: ")

                    clientSock = socket.socket(
                        socket.AF_INET, socket.SOCK_DGRAM)
                    clientSock.connect((UDP_IP, int(UDP_PORT)))

                inp = input("")

                clientSock.send(str.encode(inp))

            except KeyboardInterrupt:
                server.stop()
                print("Выход из режима")
                break

    elif mode == "!chip":
        UDP_IP = input("Введите ip: ")

        clientSock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)
        clientSock.connect((UDP_IP, int(UDP_PORT)))

    elif mode == "!chport":
        UDP_PORT = input("Введите порт: ")

        if UDP_IP != None:
            clientSock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM)
            clientSock.connect((UDP_IP, int(UDP_PORT)))

        try:
            server.setPort(UDP_PORT)
        except:
            pass

    else:
        print("Введите верный режим")

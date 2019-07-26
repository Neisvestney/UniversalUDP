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


print("Universal UDP client/server in Python")
print("Created by Neisvestney")
print("Quick Reference: \nOperable modes: 1 - client, 2 - server, 3 - client/server \nExit from - ctrl + c \nChange ip - !chip, port - !chport")
while True:
    mode = input("Mode or command:")
    if mode == "1":
        while True:
            try:
                if UDP_PORT == None or UDP_IP == None:
                    UDP_IP = input("Enter ip:")
                    UDP_PORT = input("Enter Port:")

                    clientSock = socket.socket(
                        socket.AF_INET, socket.SOCK_DGRAM)
                    clientSock.connect((UDP_IP, int(UDP_PORT)))

                inp = input("")

                clientSock.send(str.encode(inp))
                print("Sent!")

            except KeyboardInterrupt:
                print("Exit mode")
                break
    elif mode == "2":
        while True:
            try:
                if UDP_PORT == None:
                    UDP_PORT = input("Enter port:")

                server = Server(UDP_PORT)
                server.start()

                input("")

            except KeyboardInterrupt:
                server.stop()
                print("Exit mode")
                break

    if mode == "3":
        if UDP_PORT == None:
            UDP_PORT = input("Enter port:")
        server = Server(UDP_PORT)
        server.start()
        while True:
            try:
                if UDP_IP == None:
                    UDP_IP = input("Enter ip:")

                    clientSock = socket.socket(
                        socket.AF_INET, socket.SOCK_DGRAM)
                    clientSock.connect((UDP_IP, int(UDP_PORT)))

                inp = input("")

                clientSock.send(str.encode(inp))

            except KeyboardInterrupt:
                server.stop()
                print("Exit mode")
                break

    elif mode == "!chip":
        UDP_IP = input("Enter ip: ")

        clientSock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)
        clientSock.connect((UDP_IP, int(UDP_PORT)))

    elif mode == "!chport":
        UDP_PORT = input("Enter port:")

        if UDP_IP != None:
            clientSock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM)
            clientSock.connect((UDP_IP, int(UDP_PORT)))

        try:
            server.setPort(UDP_PORT)
        except:
            pass

    else:
        print("Enter the correct mode")

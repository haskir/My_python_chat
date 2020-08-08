import socket
import datetime
import random


def add_info(string, iden):
    return str(datetime.datetime.now()) + " " + str(iden) + " " + string


client_id = random.randint(0, 10000)
address = '127.0.0.1'
port = 14888

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        data = add_info(input(), client_id)
        client.connect((address, port))
        client.send(data.encode())
        print(client.recv(1024).decode())
        client.close()

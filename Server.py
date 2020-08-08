import socket


dict_of_keys = {}

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 14888))                        # Local host + port
server_socket.listen(10)                                        # Count of waiters who want to connect
print("Server is Up!")

while True:                                                     # Permanent cycle
    client_socket, remote_address = server_socket.accept()      # Accept all connections
    try:
        client_message = client_socket.recv(1024)               # Read 1024 bytes
        client_socket.send(b'1')                                # Send back a report
        print(client_message.decode())                          # Message [ Time : Client_id : message ]
    except():
        pass


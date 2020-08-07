import socket

server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(1)


while True:
    client_socket, remote_address = server_socket.accept()

    request = client_socket.recv(1024)
    if request == 'exit':
        print('goodbye!')
        break
    client_socket.send(request.upper())
    print(client_socket.getpeername(), request)
    client_socket.close()


client_socket.close()
server_socket.close()

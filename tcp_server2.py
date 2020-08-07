import socket

server_socket = socket.socket()
server_socket.bind(('', 2222))
server_socket.listen(10)


while True:
    client_socket, remote_address = server_socket.accept()

    request = client_socket.recv(1024)
    print(request.decode('utf-8'), type(request))
    if 'close' in request.decode('utf-8'):
        #client_socket.send(bytes('goodbye\n', 'utf-8'))
        client_socket.close()
        server_socket.close()
        break
    client_socket.send(request)
    client_socket.close()

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12000))
server.listen()
print('server is listening on port 12000')

connection, address = server.accept()
print('connected to client')

while True:
    data = input('server: ')
    connection.send(data.encode('utf-8'))

    recvData = connection.recv(1024).decode('utf-8')
    print('client: ' + recvData)

connection.close()

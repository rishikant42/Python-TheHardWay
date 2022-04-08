import socket

client = socket.socket()

client.connect(('localhost', 12000))

print('Connected to sever')

while True:
    recvData = client.recv(1024).decode('utf-8')

    print('server: ' + recvData)

    data = input('client: ')
    client.send(data.encode('utf-8'))

client.close()

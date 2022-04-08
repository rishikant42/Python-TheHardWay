import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8787))
server.listen()

print('server is listening on 8787')

clients = []
nicknames = []

def broadcast(msg, client):
    for c in clients:
        if c != client:
            c.send(msg.encode('utf-8'))

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            broadcast(msg, client)
        except Exception as err:
            index = clients.index(client)
            nickname = nicknames[index]
            clients.remove(client)
            nicknames.remove(nickname)
            client.close()
            break

def recieve():
    while True:
        client, addr = server.accept()

        print('Connected with {}'.format(str(addr)))

        client.send('NICK: '.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients.append(client)
        nicknames.append(nickname)

        print('Nickname is {}'.format(nickname))

        broadcast('{} joined'.format(nickname), client)

        client.send('Connected to server'.encode('utf-8'))

        t = threading.Thread(target=handle_client, args=(client,))
        t.start()

recieve()

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8989))

server.listen()

print('Server is listening on 8989')

clients = []
nicknames = []

def broadcast(msg):
    for c in clients:
        c.send(msg.encode('utf-8'))

def handle(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            broadcast(msg)
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            clients.remove(client)
            nicknames.remove(nickname)
            client.close()
            break


def accept_client_conn():
    while True:
        client, addr = server.accept()
        print('connected with {}'.format(str(addr)))
        client.send('nick'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        print('Nickname is {}'.format(nickname))
        broadcast('{} joined the chat'.format(nickname))
        clients.append(client)
        nicknames.append(nickname)

        client.send('Connected to server'.encode('utf-8'))
        t = threading.Thread(target=handle, args=(client,))
        t.start()

accept_client_conn()

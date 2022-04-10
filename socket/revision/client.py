import socket
import threading

nickname = input('Enter your nickname: ')
client = socket.socket()
client.connect(('127.0.0.1', 8989))


def write():
    while True:
        msg = input(f'msg: ')
        client.send(msg.encode('utf-8'))

def recieve():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')

            if msg == 'nick':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print('An error occur')
            client.close()
            break

t1 = threading.Thread(target=write)
t2 = threading.Thread(target=recieve)

t1.start()
t2.start()

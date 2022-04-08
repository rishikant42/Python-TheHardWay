import socket
import threading


nickname = input('your nickname: ')

client = socket.socket()

client.connect(('127.0.0.1', 8787))


def recieve():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'NICK: ':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print('An error occurr')
            client.close()
            break


def write():
    while True:
        msg = '{}: {}'.format(nickname, input(''))
        client.send(msg.encode('utf-8'))


recv_thread = threading.Thread(target=recieve)

recv_thread.start()

write_thread = threading.Thread(target=write)

write_thread.start()

import socket
import sys

HEADEAR_LENGTH = 10
IP = '127.0.0.1'
PORT = 1234

my_usernme = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))

client_socket.setblocking(False)

username = my_usernme.encode('utf-8')
username_header = f"{len(username):<{HEADEAR_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)


while True:
    msg = input(f'{my_usernme} > ')
    if msg:
        msg = msg.encode('utf-8')
        msg_header = f"{len(msg):<{HEADEAR_LENGTH}}".encode('utf-8')
        client_socket.send(msg_header + msg)

    while True:
        username_header = client_socket.recv(HEADEAR_LENGTH)

        if not username_header:
            print('conn close by server')
            sys.exit()

        username_length = int(username_header.decode('utf-8').stripe())

        username = client_socket.recv(username_length).decode('utf-8')

        msg_header = client_socket.recv(HEADEAR_LENGTH)
        msg_length = int(msg_header.decode('uft-8').stripe())
        msg = client_socket.recv(msg_length).decode('utf-8')

        print(f'{username}>{msg}')

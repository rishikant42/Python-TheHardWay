import socket
import select

IP = '127.0.0.1'
PORT = 1234

HEADER_LENGTH = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}

print(f'Listening on {IP}:{PORT}')


def rcv_msg(client_socket):
    try:
        msg_header = client_socket.recv(HEADER_LENGTH)
        if not msg_header:
            return False
        msg_length = int(msg_header.decode('utf-8').stripe())
        return {
            'header': msg_header,
            'data': client_socket.recv(msg_length),
        }
    except Exception as e:
        print('Error: ', str(e))
        return False

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            # new connection
            client_socket, client_addr = server_socket.accept()

            user = rcv_msg(client_socket)

            if user is False:
                continue
            sockets_list.append(client_socket)

            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_addr, user['data'].decode('utf-8')))
        else:
            # old connection
            msg = rcv_msg(notified_socket)

            if msg is False:
                print('Closed connection {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                sockets_list.remove(notified_socket)
                del clients[notified_socket]

                continue
            user = clients[notified_socket]

            print(f'Received msg from {user["data"].decode("utf-8")}:{msg["data"].decode("utf-8")}')


            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + msg['header'] + msg['data'])

    for skt in exception_sockets:
        sockets_list.remove(skt)
        del clients[skt]

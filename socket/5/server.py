import socket
import select

HEADER_LENGTH = 10
IP = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))

print(f"Listening on {IP}:{PORT}")

sockets_list = [server_socket]

clients = {}


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
        print("Receive msg error:", str(e))
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            # new client connection
            client_socket, client_addr = server_socket.accept()
            user = rcv_msg(client_socket)

            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print("Accepeted new conn {}:{}, username".format(*client_addr, user['data'].decode('utf-8')))
        else:
            # old connection
            msg = rcv_msg(notified_socket)

            if msg is False:
                print('Closed conn from {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]

            user = clients[notified_socket]

            print("Received msg from {} : {}".format(user['data'].decode('utf-8', msg['data'].decode('utf-8'))))

            for client_skt in clients:
                if client_skt != notified_socket:
                    client_skt.send(user['header'] + user['data'] + msg['header'] + msg['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)

        del clients[notified_socket]

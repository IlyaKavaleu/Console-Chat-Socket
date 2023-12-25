import socket
import threading

clients = []


def send_clients(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)


def get_client_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            else:
                send_clients(message, client_socket)
        except:
            break
    client_socket.close()


def main():
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind(('127.0.0.1', 1111))
    new_socket.listen(5)
    print('Start server 1111')
    while True:
        client_socket, address = new_socket.accept()
        clients.append(client_socket)
        client_name = client_socket.recv(1024).decode()
        print(client_name, 'Присоединился')
        async_get_client = threading.Thread(target=get_client_message, args=(client_socket,))
        async_get_client.start()


if __name__ == "__main__":
    main()

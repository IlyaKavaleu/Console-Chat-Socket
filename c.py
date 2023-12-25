import socket
import threading


def get_message(client_name):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break


def send_message():
    while True:
        client_message = input()
        client_socket.send(client_message.encode('utf-8'))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 1111))
client_name = input('Enter client_name: ')
client_socket.send(client_name.encode())


thread_get_message = threading.Thread(target=get_message, args=(client_name,))
thread_send_message = threading.Thread(target=send_message)
thread_get_message.start()
thread_send_message.start()

# Uncomment this to pass the first stage
import socket
from concurrent.futures import ThreadPoolExecutor
import logging


def server_thread(server_socket):
    while True:
        connection, address = server_socket.accept()
        try:
            data = connection.recv(1024).decode()
            while data:
                connection.send(f"+PONG\r\n".encode())
                data = connection.recv(1024).decode()
        except ConnectionResetError:
            pass


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(server_thread, [server_socket for i in range(3)])


if __name__ == "__main__":
    main()

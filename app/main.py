# Uncomment this to pass the first stage
import socket


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        connection, address = server_socket.accept()  # wait for client
        try:
            data = connection.recv(1024).decode()
            connection.send("+PONG\r\n".encode())
        except ConnectionResetError:
            pass


if __name__ == "__main__":
    main()

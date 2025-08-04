import os
import socket
import threading

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5555

def handle_client(client_sock):
    while True:
        data = client_sock.recv(2048)
        if not data:
            break
        # Here you'd forward to the real internet, but we'll echo for demo
        client_sock.sendall(data)
    client_sock.close()

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((SERVER_IP, SERVER_PORT))
    server_sock.listen(5)
    print("VPN server started on port", SERVER_PORT)
    while True:
        client_sock, addr = server_sock.accept()
        print("Client connected from", addr)
        threading.Thread(target=handle_client, args=(client_sock,)).start()

if __name__ == '__main__':
    main()

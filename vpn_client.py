import os
import socket
import struct
import fcntl
import threading

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_NO_PI = 0x1000

SERVER_IP = '127.0.0.1'  # Replace with your server's IP
SERVER_PORT = 5555

def create_tun():
    tun = os.open('/dev/net/tun', os.O_RDWR)
    ifr = struct.pack('16sH', b'tun0', IFF_TUN | IFF_NO_PI)
    fcntl.ioctl(tun, TUNSETIFF, ifr)
    return tun

def tun_to_sock(tun, sock):
    while True:
        packet = os.read(tun, 2048)
        if packet:
            sock.sendall(packet)

def sock_to_tun(tun, sock):
    while True:
        data = sock.recv(2048)
        if data:
            os.write(tun, data)

def main():
    tun = create_tun()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, SERVER_PORT))

    t1 = threading.Thread(target=tun_to_sock, args=(tun, sock))
    t2 = threading.Thread(target=sock_to_tun, args=(tun, sock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()

import socket
import time

UDP_IP = "255.255.255.255"
UDP_PORT = 1337

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

with open("flag.txt", "r") as f:
	flag = f.read().strip()


while True:
    message = flag.encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))    
    time.sleep(10)
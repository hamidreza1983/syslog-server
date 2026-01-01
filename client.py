import socket
from sender import send
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_IP, PORT = '192.168.87.1', 15555

while True:
    try:
        message = send()
        s.sendto(message.encode('utf-8'), (SERVER_IP, PORT))
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

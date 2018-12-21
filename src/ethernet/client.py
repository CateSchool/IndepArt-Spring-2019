import socket
from constants import *
import encode

import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Made socket.")
client_sock.connect((sys.argv[1], 19079))
print("Connected")

while True:
    data = input()
    if not data: break
    client_sock.sendall(data.encode('utf-8'))
print("Finished")
client_sock.close()
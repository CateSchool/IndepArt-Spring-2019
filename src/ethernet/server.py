import socket
from constants import *

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(("", 19079))

server_sock.listen(5)
print("Server bound and listening @ %s:%s" % (server_sock.getsockname()))

while True:
    client_sock, address = server_sock.accept()
    raw = client_sock.recv(4096)
    if not raw: break
    print(raw.decode('utf-8'))

print("Closing...")
server_sock.close()
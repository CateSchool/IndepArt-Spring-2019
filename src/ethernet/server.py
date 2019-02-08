import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(("", 19079))

server_sock.listen(5)
print("Server bound and listening @ %s:%s" % (server_sock.getsockname()))

client_sock, address = server_sock.accept()
while True:
    raw = client_sock.recv(4096)
    if len(raw) == 0: break
    print(raw.decode('utf-8'))

print("Closing...")
server_sock.close()
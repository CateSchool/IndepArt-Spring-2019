import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(("", 19079))

server_sock.listen(5)
print("Server bound and listening @ %s:%s" % (server_sock.getsockname()))

client_sock, address = server_sock.accept()
while True:
    raw = int.from_bytes(client_sock.recv(2), byteorder='little')
    if raw == 0: break

    readable = bin(raw)[2:]
    print("Recieved: ", readable[:7], "|", readable[8:])

print("Closing...")
server_sock.close()
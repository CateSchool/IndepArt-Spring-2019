import socket
from do_midi import do_midi

print("\nCreating server...")

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(("", 19079))

server_sock.listen(5)
print("Server bound and listening @ %s" % socket.gethostbyname(socket.gethostname()))

client_sock, address = server_sock.accept()
print("\nGot client at", address)
while True:
    try:
        raw = int.from_bytes(client_sock.recv(2), byteorder='little')
        if raw == 0: break

        readable = bin(raw)[2:].rjust(16, '0')
        print("Recieved: {:0>8} | {:0>8}".format(readable[:8], readable[8:]))

    except KeyboardInterrupt:
        print("Closing...")
        server_sock.close()
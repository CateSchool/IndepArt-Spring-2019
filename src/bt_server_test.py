from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("", 3))
server_sock.listen(1)

client_socket, address = server_socket.accept()
print("Found client @%s" % address)
print("Getting data...")

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print(data)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
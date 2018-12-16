from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
print("Server socket succesfully created.")
server_sock.bind(("", 3))
server_sock.listen(1)
print("Socket bound and listening.")

client_sock, address = server_sock.accept()
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
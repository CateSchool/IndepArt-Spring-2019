from bluetooth import *

server_sock=BluetoothSocket(RFCOMM)
print("Server socket succesfully created.")
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()
print("Socket bound and listening on port", port)

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
    service_id = uuid,
    service_classes = [ uuid, SERIAL_PORT_CLASS ],
    profiles = [ SERIAL_PORT_PROFILE ], 
#    protocols = [ OBEX_UUID ] 
    )

client_sock, address = server_sock.accept()
print("Found client!")
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
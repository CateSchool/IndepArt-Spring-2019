from bluetooth import *

server_sock = BluetoothSocket()
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid= "8f6f844b-a197-48d8-a2c6-da956b01cf5f" #randomly yote from http://guid-convert.appspot.com/

advertise_service(server_sock, "Gamma's Server",
    service_uuid=uuid,
    service_classes=[uuid, SERIAL_PORT_CLASS]
#   protocols = [ OBEX_UUID ] 
    )
                   
print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
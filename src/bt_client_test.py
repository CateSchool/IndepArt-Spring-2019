from bluetooth import *

print("Making socket...")
client_socket = BluetoothSocket(RFCOMM)
print("Connecting...")
client_socket.connect(("10:F0:05:75:66:D7", 3))

print("connected. type stuff")
while True:
    data = input()
    if len(data) == 0: break
    sock.send(data)

sock.close()
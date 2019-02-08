import socket #Send data
import sys #Get server ip from user
import time #Don't send data too fast

from get_gpio import get_gpio

# To get the target IP:
# If server is PC, ipconfig and look at "ethernet"
# If server is raspi, ifconfig and similar.

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Made socket.")
client_sock.connect((sys.argv[1], 19079))
print("Connected")

while True:
    client_sock.sendall(get_gpio())
    time.sleep(0.05) #20ms delay is fine by me.

print("Finished")
client_sock.close()
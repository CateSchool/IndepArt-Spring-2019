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
    gpio = get_gpio()
    readable = bin(gpio)[1:].rjust(16, '0')
    print("Sending: {:0>8} | {:0>8}".format(readable[:7], readable[8:]))
    gpio = gpio.to_bytes(2, 'little')
    client_sock.sendall(gpio)
    time.sleep(0.05) #20ms delay is fine by me.

print("Finished")
client_sock.close()
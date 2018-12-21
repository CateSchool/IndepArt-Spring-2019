from bluetooth import *

print("Searching...")

nearby_devices = discover_devices(lookup_names=True)

for name, addr in nearby_devices:
    print(addr, name)
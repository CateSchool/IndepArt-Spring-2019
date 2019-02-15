import mido
import sys

# Important! loopMIDI must be running. Otherwise I will have the big sad.
# This will send data to loopMIDI, which sends it to FL. Set the port there to
# whatever you want. I'll use 79.
# This sends all data to Channel 1 on that port.
# It sends the analog data to ctrl 0 of that port, and sends the digital
# data to ctrls 1-7.

print("Initializing Mido...")

output_names = mido.get_output_names()
print("Found these ports:", output_names)
output_name = None
for name in output_names:
    if "python_to_fl" in name:
        output_name = name
        break
else:
    raise RuntimeError("python_to_fl wasn't found in any currently open MIDI ports!")

print("Identified `%s' as python_to_fl." % output_name)
outport = mido.open_output(output_name)
print("Successfully created outport.")

print("Finished initializing Mido.")

def do_midi(raw):
    digital = raw >> 8 #8 most significant bits
    analog = raw & 0xff #8 least significant bits

    # analog message can only be from 0 - 127: must divide given value by 2.
    analog_msg = mido.Message('control_change', value=int(analog/2), channel=0, control=0)

    # digital message: either 0 or 127. Takes up channels 1-7 
    digital_msgs = [mido.Message('control_change', value=((digital >> bit) & 1) * 127,
        channel=0, control=8-bit) for bit in range(7, -1, -1)]

    for msg in [analog_msg] + digital_msgs:
        outport.send(msg)
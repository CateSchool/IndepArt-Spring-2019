"""
midi.py
Returns 24-byte long values encoding MIDI data.
"""

from constants import *

def sig_control(channel, controller, value):
    if channel > 0b1111: return
    if controller > 0b01111111: return
    if value > 0b01111111: return

    output = M_CONTROL | channel
    output <<= 8
    output |= controller
    output <<= 8
    output |= value
    print(len(bin(output)))
    print(bin(output))

if __name__ == "__main__":
    sig_control(0, 2, 80)
from constants import *

def text(inp):
    inp = sum([ord(char) for char in inp])
    inp &= 0x00ffffff
    inp |= (PRINT << 24)
    return bytes(inp)
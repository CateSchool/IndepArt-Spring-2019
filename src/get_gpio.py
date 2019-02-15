# Run on the pi. Sends data to the PC (server)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

data_pin_ids = [23, 24, 25, 12, 16, 20, 21]
for pin in data_pin_ids:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #data!

# For now, send one byte.
# The first bit is always 1, to make sure the server doesn't shut down from a
#null byte.
# The remaining bits are to trigger MIDI controls 0-6.
def get_gpio():
    digital_pins = 0
    for c, pin_id in enumerate(data_pin_ids):
        digital_pins |= GPIO.input(pin_id) << c

    analog_pot = int(input()) # For now
    result = (digital_pins << 8) | analog_pot #1 value
    print("get_gpio: ", bin(result))
    return result
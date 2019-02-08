# Run on the pi. Sends data to the PC (server)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #trigger pin
data_pin_ids = [23, 24, 25, 12, 16, 20, 21]
for pin in data_pin_ids:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #data!

# For now, send one byte.
# The first bit is always 1, to make sure the server doesn't shut down from a
#null byte.
# The remaining bits are to trigger MIDI controls 0-6.
def get_gpio():
    result = 0
    for c, pin_id in enumerate(data_pin_ids):
        print(GPIO.input(pin_id))
        result |= GPIO.input(pin_id) << c
    result = result.to_bytes(1)
    print("Sending", result)
    return result
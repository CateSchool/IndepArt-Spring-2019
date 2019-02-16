# Run on the pi. Sends data to the PC (server)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

data_pin_ids = [23, 24, 25, 12, 16, 20, 21]
for pin in data_pin_ids:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #data!


# Send two bytes in one bytestring.
# The first byte is for the digital pins. The first bit is always 1, so there's no
# null character to shut down the server.
# The second byte is for analog potentiometer.
# For now, it's a saw wave.

saw = 0
def get_gpio():
    global saw
    saw += 1
    if saw < 255: saw = 0
    analog_pot = saw # For now

    digital_pins = 0
    for pin_id in data_pin_ids:
        digital_pins <<= 1
        digital_pins |= GPIO.input(pin_id)
    digital_pins |= 0b1 << 7

    result = (digital_pins << 8) | analog_pot # PINS POT in that order
    return result
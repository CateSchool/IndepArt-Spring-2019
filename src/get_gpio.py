# Run on the pi. Sends data to the PC (server)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

data_pin_ids = [23, 24, 25, 12, 16, 20, 21]
for pin in data_pin_ids:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #data!


# Send two bytes in one bytestring.
# The first byte is for the digital pins. The first bit is always 0, so there's no
# null character to shut down the server.
# The second byte is for analog potentiometer.
# For now, it's a user input in the console.
def get_gpio():
    analog_pot = int(input()) # For now

    digital_pins = 0
    for c, pin_id in enumerate(data_pin_ids):
        digital_pins |= GPIO.input(pin_id) << c
    digital_pins |= 0b1 << 7

    result = (digital_pins << 8) | analog_pot # PINS POT in that order
    print("get_gpio: ", bin(result))
    return result
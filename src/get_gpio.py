# Run on the pi. Sends data to the PC (server)

# Init GPIO...
print("Initializing GPIO...")
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

data_pin_ids = [23, 24, 25, 12, 16, 20, 21]
for pin in data_pin_ids:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #data!
print("GPIO intialized.")

# Init Spidev...
print("Initializing Spidev...")
import spidev
spi = spidev.SpiDev()
spi.open(0, 0) # Bus 0 (?), channel 0 (using pin CE0)
spi.max_speed_hz = 1000000 # the secret sauce that makes this work
print("Spidev intialized.")


# get_gpio
# Send two bytes in one bytestring.
# The first byte is for the digital pins. The first bit is always 1, so there's no
# null character to shut down the server.
# The second byte is for analog potentiometer.
# Technically, the TLC549C returns the value of the potentiometer the last time
# I requested data, not the current state of the pot. 
# But I'm requesting fast enough it should be OK.
# (foreshadowing?)

def get_gpio():
    # Read potentiometer
    analog_pot = spi.readbytes(1)[0]

    # Read pushbuttons
    digital_pins = 0
    for pin_id in data_pin_ids:
        digital_pins <<= 1
        digital_pins |= GPIO.input(pin_id)
    digital_pins |= 0b1 << 7

    result = (digital_pins << 8) | analog_pot # PINS POT in that order
    return result
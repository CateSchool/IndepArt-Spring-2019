"""A class used to get debounced inputs from a pushbutton"""

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Debounced:
    def __init__(self, pin, wait=2):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #init the pin
        self.pin_id = pin
        self.default_wait = wait #How many cycles to wait before a switch is "good"
        self.wait = 0 # A counter
        self.can_send = True # if it wasn't pressed recently

    def __bool__(self): #bc why waste characters?
        if self.wait > 0: return false

        if GPIO.input(self.pin_id):
            self.wait = self.default_wait # Reset counter
            return true
        else: return false

if __name__ == "__main__":
    # a test
    my_dber = Debounced(18)
    counter = 0
    while True:
        if my_dber: counter += 1
        print(counter)

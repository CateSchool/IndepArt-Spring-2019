import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Initialize pins
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #trigger pin
data_pin_ids = [23, 24, 25, 12, 16, 20, 21, 5]
for pin in data_pin_ids:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #data!

def on_trigger():
	result = 0
	for c, pin_id in enumerate(data_pin_ids):
		print(GPIO.input(pin_id))
		result |= GPIO.input(pin_id) << c
	print("Data recieved: {}".format(hex(result)))


is_held = False
try:
	while True:
		if GPIO.input(18):
			if not is_held:
				on_trigger()
				is_held = True
		else:
			is_held = False
except KeyboardInterrupt:
	print("Exiting...")
	GPIO.cleanup()


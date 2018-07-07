"""
Continously prints the distance detected by the HC-SR04 Ultrasonic Range Sensor
Usage: python distance.py
To Stop: CTRL+C

Connecting the Sensor
Connect sensor GND to Raspberry Pi GND
Connect Pin 1 of 2K resistor to GND
Connect Pin 2 of 2K resistor to GPIO 24
Connect Pin 1 of 1K resistor to GPIO 24
Connect Pin 2 of 1K resistor to ECHO pin of sensor
Connect TRIG pin of sensor to GPIO 23
Connect VCC pin of sensor to Raspberry Pi 5V

Note: Resistors are used to create a voltage divider circuit.
The output of the ECHO pin is 5V, but the Raspberry Pi can only handle 3.3V inputs
"""

import RPi.GPIO as GPIO
import time

# Use Broadcom Pin Mappings
GPIO.setmode(GPIO.BCM)

# Output pin that triggers the sensor (Pin 16)
triggerPin = 23

# Input pin that reads return signal from the sensor (Pin 18)
echoPin = 24

GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
	while (True):
		# Initially turn the trigger off, wait a bit for it to settle
		GPIO.output(triggerPin, False)
		time.sleep(1.1)

		# Triggering the module requires a 10 microseccond pulse
		GPIO.output(triggerPin, True)
		time.sleep(0.00001)
		GPIO.output(triggerPin, False)

		# Get the time just before the Echo pin goes HIGH
		while GPIO.input(echoPin) == 0:
			pulseStart = time.time()

		# Get the time just before the signal goes from HIGH back to LOW
		# The echo pin is HIGH for the amount of time it takes for the pulse
		# to go out and come back
		# Think of it as the round trip time for an acknowlegement
		while GPIO.input(echoPin) == 1:
			pulseEnd = time.time()

		pulseDuration = pulseEnd - pulseStart

		# Speed of Sound in cm/sec
		soundSpeed = 34300

		# The distance is actually the round trip, so we only need half of it
		distance = pulseDuration * soundSpeed/2
		distance = round(distance, 2)

		print "Distance: ", distance, " cm"
except KeyboardInterrupt:
	print "Exiting . . ."

# Release the GPIO pins
GPIO.cleanup()

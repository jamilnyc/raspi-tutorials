# Interpretted with Python 3
from gpiozero import LED, Button
from time import sleep
from random import uniform
import time

# Declare and assign hardware variables
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# Get user names from the command line input
left_name = input('Left player name is ')
right_name = input('Right player name is ')

# For keeping track of the player's points
left_points = 0
right_points = 0

def pressed(button):
    # No points if it is not lit
    if not led.is_lit:
        return
    
    # Declare global because the variables will be written
    global right_points
    global left_points

    # TODO: Print averages of reaction time

    # variable led will only be read, no need to declare global
    led.off()
    press_time = time.time()

    if button.pin.number == 14:
        left_points += 1
        print(left_name + ' won the round. ' + str(left_points) + ' Point(s)!')
    else:
        right_points += 1
        print(right_name + ' won the round. ' + str(right_points) + ' Point(s)!')

    reaction_time = (press_time - lit_time)
    print('Reaction time: %.3f sec' % reaction_time)

# Keep track of the time the LED turned on
lit_time = 0

# Set button press listeners
right_button.when_pressed = pressed
left_button.when_pressed = pressed

# Loop forever . . . or until you hit CTRL+C
while True:
    # Turn the LED on and off for random periods of time
    # between 5 and 10 seconds
    led.on()
    lit_time = time.time()
    sleep(uniform(5, 10))
    led.off()
    sleep(uniform(5, 10))

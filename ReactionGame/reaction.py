# Interpretted with Python 3
from gpiozero import LED, Button
from time import sleep
from random import uniform

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
    # Declare global because the variables will be written
    global right_points
    global left_points

    # TODO: Only calculate points when the LED is on
    # TODO: Print the reaction time (time between press and reaction time)
    # TODO: Print averages of reaction time

    # variable led will only be read, no need to declare global
    led.off()

    if button.pin.number == 14:
        left_points += 1
        print(left_name + ' won the round. ' + str(left_points) + ' Points!')
    else:
        right_points += 1
        print(right_name + ' won the round. ' + str(right_points) + ' Points!')

# Set button press listeners
right_button.when_pressed = pressed
left_button.when_pressed = pressed

# Loop forever . . . or until you hit CTRL+C
while True:
    # Turn the LED on and off for random periods of time
    # between 5 and 10 seconds
    led.on()
    sleep(uniform(5, 10))
    led.off()
    sleep(uniform(5, 10))

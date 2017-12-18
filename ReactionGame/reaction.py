# Interpretted with Python 3
from gpiozero import LED, Button
from time import sleep
from random import uniform
import time

# Declare and assign hardware variables
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# For keeping track of the player's points
left_points = 0
right_points = 0

# For tracking average reaction times
left_reaction_total = 0
right_reaction_total = 0

def print_instructions():
    print("######################################")
    print('Reaction Game - 2 Players')
    print('Directions:')
    print('* Enter player names')
    print('* Press your button when it lights up')
    print('* To end the game, hit CTRL+C')
    print('######################################')

def print_hits(name, points):
    message = name + ' won this round. ' + str(points) + ' '
    if points > 1:
        message += 'Points!'
    else:
        message += 'Point!'
        
    print (message)

def print_misses(name):
    message = 'Watch it, ' + name + '! It is not on.'
    print(message)

def pressed(button):
    # No points if it is not lit
    if not led.is_lit:
        if button.pin.number == 14:
            print_misses(left_name)
        else:
            print_misses(right_name)
        return
    
    # Declare global because the variables will be written
    global right_points
    global left_points
    global right_reaction_total
    global left_reaction_total

    # TODO: Track "false" hits (when LED is off)

    # variable led will only be read, no need to declare global
    led.off()
    press_time = time.time()
    reaction_time = (press_time - lit_time)
    reaction_average = 0

    if button.pin.number == 14:
        left_points += 1
        left_reaction_total += reaction_time
        reaction_average = left_reaction_total / left_points
        print_hits(left_name, left_points)
    else:
        right_points += 1
        right_reaction_total += reaction_time
        reaction_average = right_reaction_total / right_points
        print_hits(right_name, right_points)

    print('Reaction time: %.3f sec (Avg. %.3f sec)' % (reaction_time, reaction_average))

# Keep track of the time the LED turned on
lit_time = 0

# Set button press listeners
right_button.when_pressed = pressed
left_button.when_pressed = pressed

print_instructions()

# Get user names from the command line input
left_name = input('Left player name is ')
right_name = input('Right player name is ')

# Loop forever . . . or until you hit CTRL+C
while True:
    # Turn the LED on and off for random periods of time
    # between 5 and 10 seconds
    led.on()
    lit_time = time.time()
    sleep(uniform(1, 4))
    led.off()
    sleep(uniform(1, 4))

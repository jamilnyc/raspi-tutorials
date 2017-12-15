from gpiozero import LED, Button
from time import sleep
from random import uniform


led = LED(4)
right_button = Button(15)
left_button = Button(14)
left_name = input('left player name is ')
right_name = input('right player name is ')
left_points = 0
right_points = 0

def pressed(button):
    global right_points
    global left_points
    led.off()
    if button.pin.number == 14:
        left_points += 1
        print(left_name + ' won the round. ' + str(left_points) + ' Points!')
    else:
        right_points += 1
        print(right_name + ' won the round. ' + str(right_points) + ' Points!')

right_button.when_pressed = pressed
left_button.when_pressed = pressed

while True:
    led.on()
    sleep(uniform(5, 10))
    led.off()
    sleep(uniform(5, 10))


# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import left, right, forward, backward, speed
import room

# Draw the Level 1 version of the room
window = room.draw_room(level = 1)

###
# Start your code here
side_length = 5  
circumference = side_length * 100
radius = circumference/(3.14*2)
def draw_circle():
    for i in range(1,101):
        speed(i)
        forward(side_length)
        right(360/100)
draw_circle()
draw_circle()
right(90)

def draw_interior(): 
    forward(radius)
    left(45)
    forward(radius)
    left(180)
    forward(radius)
    for i in range(2):
        left(135)
        forward(radius)
        left(180)
        forward(radius)
    left(45)
    forward(radius)
    left(180)

draw_interior()
draw_interior()



 
 
# End your code here
###
 
window.exitonclick()
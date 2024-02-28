# File: HW3B
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E
#
# Date: 9/20/2023
# Description of program: Draws a user-determined shape

import turtle

shapeAsk = str(input(f'Would you like to draw a circle, square, or triangle? '))
colorAsk = str(input(f'What color would you like? '))
sizeAsk = int(input(f'What size would you like? '))
fillAsk = str(input(f'Would you like it filled? '))

#Set the pen for drawing
if fillAsk == "yes":
    turtle.begin_fill()

turtle.color(colorAsk)


#Execute a draw command based on user input
if shapeAsk == "circle":
    turtle.circle(sizeAsk)
    
if shapeAsk == "square":
    
    count = 0
    while count < 5:
        turtle.forward(sizeAsk)
        turtle.left(90)
        count += 1
        
if shapeAsk == "triangle":
    
    count = 0
    while count < 4:
        turtle.forward(sizeAsk)
        turtle.left(120)
        count += 1


#Set pen after drawing
if fillAsk == "yes":
    turtle.end_fill()

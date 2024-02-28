# File: HW4A
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E
#
# Date: 9/25/2023
#Description of program: Draws 10 concentric squares

import turtle

for num in range(200, 0, -20):

    for turn in range(4):
        turtle.forward(num)
        turtle.right(90)

    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()

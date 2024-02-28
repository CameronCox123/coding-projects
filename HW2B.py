##HW2B
##Cameron Cox
##UTEID: cpc2526your EID
##CS 303E
##9/14/2023

    ##Draws the Apple logo

import turtle

    #Begin the fill and position the mouse
turtle.begin_fill()
turtle.right(22)

    #Draw the curvy top
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)

turtle.right(15)
turtle.backward(13)
turtle.right(15)
turtle.backward(13)
turtle.right(15)
turtle.backward(13) 

turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)

    #Draw the left side
turtle.left(20)
turtle.circle(-120, -75)
turtle.left(23)

    #Draw the curvy bottom
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)

turtle.right(15)
turtle.backward(13)
turtle.right(15)
turtle.backward(13)
turtle.right(15)
turtle.backward(13)

turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(15)
turtle.backward(13)
turtle.left(20)

    #Draw the right side and bite mark
turtle.circle(-120, -20)
turtle.right(75)
turtle.circle(-45, 170)
turtle.left(-75)
turtle.circle(-50, -38)
turtle.end_fill()

    #Move the pen to draw the leaf
turtle.penup()
turtle.setx(-70)
turtle.sety(30)
turtle.pendown()

    #Draw the leaf
turtle.begin_fill()
turtle.left(110)
turtle.circle(-40, 100)
turtle.right(83)
turtle.circle(-40, 100)
turtle.end_fill()

    #Move pen to corner
turtle.penup()
turtle.setx(200)
turtle.sety(-200)
turtle.pendown()

ts = turtle.getscreen()
ts.getcanvas().postscript(file='Cameron_Cox.eps')
turtle.done()

#space Invaders
#Screen setup

import turtle

#setup
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space Invaders")



#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup() #change default start point of pen to border we want instead of the center
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600) #forward
    border_pen.lt(90) #left turn 90deg

#turtle.done
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup() #not drawing
player.speed(0)
player.setposition(0,-250)#bottom right border
player.setheading(90)

#program ends and screen closes, we use this to keep it open
#input was originally raw_input
delay = input("Press enter to finish.")
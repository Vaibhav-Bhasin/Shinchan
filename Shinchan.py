
""" Vabhav Bhasin"""

from turtle import *

# Functions for drawing Shinchan

# Definition the position of the pen
def myPosition(x, y):
    penup()
    goto(x, y)
    pendown()


# V function
def v():
    fillcolor('#ffec40')
    begin_fill()
    right(25)
    forward(20)
    right(45)
    forward(20)
    left(70)
    forward(90)
    left(95)
    forward(75)
    left(85)
    forward(175)
    left(85)
    forward(75)
    left(95)
    forward(90)
    left(85)
    forward(18)
    end_fill()

# Left leg funtion
def leftLeg():
    myPosition(-39,-25)
    fillcolor("#ffd699")
    begin_fill()
    right(89)
    forward(25)
    right(90)
    forward(50)
    right(90)
    forward(20)
    right(85)
    forward(50)
    end_fill()


# Left sock function
def leftSock():
    myPosition(-36,-78)
    fillcolor("#ffffff")
    begin_fill()
    right(90)
    circle(80,13)
    right(110)
    forward(22)
    right(85)
    forward(19)
    right(90)
    forward(21)
    end_fill()



# Left Shoe function
def leftShoe():
    myPosition(-69,-112)
    fillcolor("#b5ae60")
    begin_fill()
    right(90)
    left(5)
    forward(56)
    left(105)
    forward(13)
    left(75)
    forward(20)
    right(90)
    forward(15)
    circle(10,15)
    left(80)
    forward(4)
    circle(10,15)
    left(40)
    circle(20,15)
    forward(10)
    right(45)
    forward(15)
    circle(25,25)
    end_fill()

# Rigth leg function
def rightLeg():
    myPosition(60,-28)
    fillcolor("#ffd699")
    begin_fill()
    #right(90)
    left(128)
    forward(25)
    right(95)
    forward(55)
    right(90)
    forward(20)
    right(85)
    forward(55)
    end_fill()

# Rigth sock function
def rightSock():
    myPosition(64,-79)
    fillcolor("#ffffff")
    begin_fill()
    right(90)
    circle(90,14)
    right(110)
    forward(23)
    right(90)
    forward(15)
    right(80)
    forward(21)
    end_fill()

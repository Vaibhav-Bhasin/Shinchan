
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

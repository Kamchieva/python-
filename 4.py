from turtle import *

hideturtle()
color('black', 'magenta')
def left_turn():
    for i in range(10):
        forward(15)
        left(9)
def petal():
    begin_fill()
    left_turn()
    left(90)
    left_turn()
petal()

bye()
from turtle import Turtle
angle_def = 45


turtle = Turtle()


def move(steps=50):
    turtle.fd(steps)


def turn_right(angle=angle_def):
    turtle.right(angle)


def turn_left():
    turn_right(angle=angle_def*-1)


def back(steps=-10):
    move(-10)


def undo(steps=3):
    turtle.penup()
    for i in range(steps):
        turtle.undo()
    turtle.pendown()


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


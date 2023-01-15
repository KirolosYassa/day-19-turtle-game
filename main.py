from turtle import  Screen
from functions import *

screen = Screen()

turtle.speed("fastest")
screen.listen()
# for moving forward
screen.onkey(key="Up", fun=move)
screen.onkey(key="w", fun=move)
screen.onkey(key="space", fun=move)
# for moving Right
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="d", fun=turn_right)
# for moving Left
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="a", fun=turn_left)
# for moving backward
screen.onkey(key="Down", fun=back)
screen.onkey(key="s", fun=back)
# for clearing
screen.onkey(key="z", fun=undo)
# for undo
screen.onkey(key="c", fun=clear)

screen.exitonclick()

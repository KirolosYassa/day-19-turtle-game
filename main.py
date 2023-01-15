from turtle import Screen
from generateTurtles import *

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bet your winner turtle", prompt="What color will the winner turtle be?")
print(user_bet)
generate_turtles()

screen.exitonclick()

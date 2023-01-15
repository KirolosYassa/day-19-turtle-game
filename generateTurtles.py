from Tur import *

colors = ["red", "purple", "yellow", "blue", "green", "orange"]


def generate_turtles():
    turtles = []
    position_index = 1

    for color in colors:
        t = Tur(color=color)
        t.start_position(position=position_index)
        turtles.append(t)
        position_index += 1

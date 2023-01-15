from turtle import Turtle, Screen
import random as r

width = 800
height = 400
max_steps = (width/100) * 3
angle_def = 45
start_x = (width/2) * -1
start_y = (height/2)
flag = abs(start_x) - 20


class Tur:

    def __init__(self, color):
        self.self = Turtle("turtle")
        self.self.speed("slow")
        self.self.color(color)
        self.color = color

    def get_color(self):
        return self.color

    def start_position(self, position=1):
        self.self.penup()
        self.self.goto(x=start_x+20, y=start_y-(position*55))
        self.self.pendown()

    def arrived(self):
        x = self.self.xcor()
        # print(f"{self.get_color()} X = {x}, and Flag = {flag}")
        if x >= flag:
            return True
        else:
            return False

    def move(self, steps=50):
        self.self.penup()
        self.self.fd(steps)
        self.self.pendown()

    # EXTRA FUNCTIONS
    def turn_right(self, angle=angle_def):
        self.self.right(angle)

    def turn_left(self, angle=angle_def*-1):
        self.turn_right(self, angle=angle_def*-1)

    def back(self, steps=-10):
        self.move(-10)

    def undo(self, steps=3):
        self.self.penup()
        for i in range(steps):
            self.self.undo()
        self.self.pendown()

    def clear(self):
        self.self.clear()
        self.self.penup()
        self.self.home()
        self.self.pendown()


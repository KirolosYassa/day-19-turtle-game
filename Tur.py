from turtle import Turtle

angle_def = 45
start_x = -250
start_y = 200


class Tur:

    def __init__(self, color):
        self.self = Turtle("turtle")
        self.self.color(color)

    def start_position(self, position=1):
        self.self.penup()
        self.self.goto(x=start_x+20, y=start_y-(position*55))
        self.self.pendown()

    def move(self, steps=50):
        self.self.fd(steps)

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


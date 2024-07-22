from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.new_location()

    def new_location(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

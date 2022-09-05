from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))

    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))

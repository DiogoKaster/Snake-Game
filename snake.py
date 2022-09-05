from turtle import Turtle

start_pos = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in start_pos:
            self.increase_size(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[seg_num - 1].xcor()
            next_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=next_x, y=next_y)
        self.segments[0].fd(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def extend_snake(self):
        self.increase_size(self.segments[-1].position())

    def increase_size(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.pu()
        t.goto(position)
        self.segments.append(t)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

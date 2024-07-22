from turtle import Turtle

START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake(Turtle):
    def __init__(self):
        super(Snake, self).__init__()
        self.is_game = True
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed = 20

    def create_snake(self):
        for pos in START:
            self.new_segment(pos)

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            old_x = self.segments[n - 1].xcor()
            old_y = self.segments[n - 1].ycor()
            self.segments[n].goto((old_x, old_y))
            # this means that the movement of all the segments are related to eachother
            # so if the snake goes left, all the rest of the segments follow consequently
        self.head.forward(self.speed)

        if self.head.xcor() > 600 or self.head.ycor() > 600:
            pass

    def up(self):
        if self.head.heading()!= 270.0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def rightt(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def leftt(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)

    def new_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        new_segment.showturtle()
        self.segments.append(new_segment)

    def extend(self):
        self.new_segment(self.segments[-1].position())

    def delete_snake(self):
        self.hideturtle()





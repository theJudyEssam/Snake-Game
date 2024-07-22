from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.goto(-20, 270)
        self.pencolor("white")
        self.score = 0
        self.write(arg=f"Scoreboard:  {self.score}", align="center", font=("Arial", 16, 'normal'))
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Scoreboard:  {self.score}", align="center", font=("Arial", 16, 'normal'))

    def reset_score(self):
        self.penup()
        self.clear()
        self.score = 0
        self.goto(-20, 270)
        self.write(arg=f"Scoreboard:  {self.score}", align="center", font=("Arial", 16, 'normal'))

    def game_over(self):

        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=("Arial", 16, 'normal'))

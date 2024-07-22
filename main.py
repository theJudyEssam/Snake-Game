import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from Score import Score
import time

t = Turtle()
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("The Amazing Game of Snake")
s.tracer(0)


def game():
    snake = Snake()
    food = Food()
    score = Score()

    s.listen()
    s.onkey(snake.up, "Up")
    s.onkey(snake.down, "Down")
    s.onkey(snake.rightt, "Right")
    s.onkey(snake.leftt, "Left")
    is_game = True
    while is_game:
        s.update()  # this update the screen everytime ALL the segments move
        snake.move()
        time.sleep(0.1)

        if snake.head.distance(food) < 15:
            food.new_location()
            snake.extend()
            score.add_score()

        if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
            score.game_over()
            is_game = False

        for i in range(1, len(snake.segments)):
            if snake.head.distance(snake.segments[i]) < 10:
                score.game_over()
                is_game = False

    reset_game = turtle.textinput("Game Over", "Do you want to play again? (Y/N)")
    if reset_game == "y" or reset_game == "Y":
        for seg in snake.segments:
            seg.hideturtle()
        food.hideturtle()
        score.reset_score()
        game()
    else:
        s.bye()


game()
s.exitonclick()

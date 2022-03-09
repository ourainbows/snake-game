from turtle import Turtle, Screen
import time

from snake import Snake

# board game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("orange")
screen.title("Snake Game")
#disable default Turtle animation
screen.tracer(0)

my_snake = Snake()

#snake animation
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)
    my_snake.move()

screen.exitonclick()
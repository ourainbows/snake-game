from turtle import Screen
import time

from food import Food
from snake import Snake
from score import Score

# board game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("orange")
screen.title("Snake Game")
#disable default Turtle animation
screen.tracer(0)

# create snake
snake = Snake()

# create food
food = Food()

# create score 
score = Score()

# listen keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# snake animation
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    
    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
        
    # snake collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
        
screen.exitonclick()
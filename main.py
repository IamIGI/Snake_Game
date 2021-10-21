from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

BOUNDRY = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)    # turning off the trace of animation
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # adding delay for 1 sec
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    #detect collision with wall
    if snake.head.xcor()>BOUNDRY  or snake.head.xcor() < -BOUNDRY  or snake.head.ycor() >BOUNDRY  or snake.head.ycor() < -BOUNDRY :
        score.game_over()
        game_is_on = False

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False
    #i


screen.exitonclick()
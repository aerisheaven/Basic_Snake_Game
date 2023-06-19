import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
import keyboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game: Python Turtle ver")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

snake_alive = True
while snake_alive:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.generate_food()
        scoreboard.update()
        snake.create_snake(False)

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
        food.generate_food()
        # scoreboard.game_over()
        # snake_alive = False

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            food.generate_food()
            # scoreboard.game_over()
            # snake_alive = False

    if keyboard.is_pressed("Escape"):
        screen.bye()

screen.exitonclick()

from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # tuple
MOVE_DISTANCE = 20
RIGHT = 0.0
UP = 90.0
DOWN = 270.0
LEFT = 180.0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake(True)
        self.head = self.snake_body[0]

    def create_snake(self, boolean):
        if boolean:
            for position in START_POSITIONS:
                snake = Turtle(shape="square")
                snake.color("white")
                snake.penup()
                snake.setpos(position)
                self.snake_body.append(snake)
                boolean = False
        else:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.setpos(self.snake_body[len(self.snake_body)-1].pos())
            self.snake_body.append(snake)

    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            move_to = self.snake_body[snake - 1].pos()
            self.snake_body[snake].goto(move_to)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

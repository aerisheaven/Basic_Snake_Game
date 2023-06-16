from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.generate_food()
        self.food_coordinates = self.pos()

    def generate_food(self):
        self.setpos(random.randint(-280, 280), random.randint(-280, 280))

    # def eat_food(self, snake_list, food_position):
    #     if snake_list[0] == food_position:


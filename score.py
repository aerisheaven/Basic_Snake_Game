# turtle.write((0, 0), True)

from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGN, font=FONT)

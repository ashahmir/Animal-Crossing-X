from turtle import Turtle
FONT = ("Michroma", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290,260)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", font=FONT, align="left")

    def end_game(self):
        self.goto(-150,-20)
        self.write("GAME OVER!", font=FONT, align="left")
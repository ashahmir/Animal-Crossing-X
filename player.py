import turtle
from turtle import Turtle
import time
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.right(-90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        time.sleep(1)
        self.goto(STARTING_POSITION)

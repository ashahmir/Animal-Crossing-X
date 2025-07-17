from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def produce_car(self):
        chance = random.randint(0,6)
        if chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randrange(-250,250, 20)
            car.goto(300, random_y)
            self.cars.append(car)

    def move_car(self):
        for cars in self.cars:
            cars.backward(self.car_speed)

    def lev_up(self):
        self.car_speed += MOVE_INCREMENT

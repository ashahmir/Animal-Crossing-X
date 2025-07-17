import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(fun=player.up, key="Up")
screen.onkeypress(fun=player.up, key="w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.produce_car()
    car_manager.move_car()

    for cars in car_manager.cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.end_game()

    if player.ycor() > 300:
        player.level_up()
        car_manager.lev_up()
        scoreboard.update_level()

screen.exitonclick()
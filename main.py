from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=400, height=500)
screen.bgcolor('black')
screen.tracer(0)
screen.title('SNAKE GAME 3000')

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    
    snake.movement()
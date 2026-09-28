# 실습 과제 진행
import math
from pico2d import *

def move_circle():
    print("circle")
    for degree in range(0,360,5):
        theta = math.radians(degree)
        clear_canvas()
        grass.draw(400, 30)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        character.draw(x, y)
        update_canvas()
    pass

def move_rectangle():
    print("rectangle")

    pass

def move_triangle():
    print("triangle")
    pass

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()
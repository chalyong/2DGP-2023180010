# 실습 과제 진행
import math
from pico2d import *

def move_circle():
    print("circle")
    rad = 0
    while rad < 2 * math.pi:
        clear_canvas()
        grass.draw(400, 30)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)
        character.draw(x, y)
        update_canvas()
        rad += 0.001
    pass

def move_rectangle():
    print("rectangle")
    x = 0
    y = 90
    while x < 900:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        x += 1
        update_canvas()
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
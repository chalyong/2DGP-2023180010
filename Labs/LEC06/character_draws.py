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
        delay(0.02)
    pass

def move_top():
    print("top")
    pass

def move_right():
    print("right")
    pass

def move_bottom():
    print("bottom")
    pass

def move_left():
    print("left")
    pass

def move_rectangle():
    print("rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
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
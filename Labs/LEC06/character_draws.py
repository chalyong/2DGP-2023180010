# 실습 과제 진행
import math
from pico2d import *

def move_circle():
    print("circle")
    for degree in range(0,360,5):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)
    pass

def move_top():
    print("top")
    for x in range(50, 750, 5):
        draw_character(x, 550)
    pass

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.02)

def move_right():
    print("right")
    for y in range(550, 50, -5):
        draw_character(750, y)
    pass

def move_bottom():
    print("bottom")
    for x in range(750, 50, -5):
        draw_character(x, 50)
    pass

def move_left():
    print("left")
    for y in range(50, 550, 5):
        draw_character(50, y)
    pass

def move_rectangle():
    print("rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_tri_left():
    print("t_left")
    for x in range(50, 400, 5):
        y = 200 + (x - 50) * (400 - 100) / (400 - 50)
        draw_character(x, y)
    pass

def move_tri_right():
    print("t_right")
    for x in range(400, 750, 5):
        y = 200 + (750 - x) * (400 - 100) / (750 - 400)
        draw_character(x, y)
    pass

def move_tri_bottom():
    print("t_bottom")
    for x in range(750, 50, -5):
        draw_character(x, 200)
    pass

def move_triangle():
    print("triangle")
    move_tri_left()
    move_tri_right()
    move_tri_bottom()
    pass

open_canvas(800, 600)
character = load_image('character.png')

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()
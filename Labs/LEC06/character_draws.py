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
    mv_mode = 0
    while mv_mode < 4:
        if mv_mode == 0:
            x = 20
            y = 90
            while x < 780:
                clear_canvas()
                grass.draw(400, 30)
                character.draw(x, y)
                x += 0.25
                update_canvas()
        elif mv_mode == 1:
            x = 780
            y = 90
            while y < 550:
                clear_canvas()
                grass.draw(400, 30)
                character.draw(x, y)
                y += 0.25
                update_canvas()
        elif mv_mode == 2:
            x = 780
            y = 550
            while x > 20:
                clear_canvas()
                grass.draw(400, 30)
                character.draw(x, y)
                x -= 0.25
                update_canvas()
        elif mv_mode == 3:
            x = 20
            y = 550
            while y > 90:
                clear_canvas()
                grass.draw(400, 30)
                character.draw(x, y)
                y -= 0.25
                update_canvas()
        mv_mode += 1
    pass

def move_triangle():
    print("triangle")
    mv_mode = 0
    while mv_mode < 3:
        if mv_mode == 0:
            x = 20
            y = 90
            while x < 780:
                clear_canvas()
                grass.draw(400, 30)
                character.draw(x, y)
                x += 0.25
                update_canvas()
        mv_mode += 1
    
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
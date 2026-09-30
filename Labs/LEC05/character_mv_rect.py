from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
mvmd = 0
while True:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

    if mvmd == 0:
        x += 2
        if x > 780:
            mvmd = 1
    elif mvmd == 1:
        y += 2
        if y > 560:
            mvmd = 2
    elif mvmd == 2:
        x -= 2
        if x < 20:
            mvmd = 3
    elif mvmd == 3:
        y -= 2
        if y < 90:
            mvmd = 0
    delay(0.01)

delay(2)
close_canvas()
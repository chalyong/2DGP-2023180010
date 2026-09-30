from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 300
r = 200
rad = 0
while True:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

    rad += 0.01

    x = 400 + r * math.cos(rad)
    y = 300 + r * math.sin(rad)

    delay(0.01)

delay(2)
close_canvas()
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here
action = 0

def draw_animation(act):
    frame = 0
    for x in range(0, 800, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(
            frame * 100, act * 100,
            100, 100,
            x, 90
        )
        update_canvas()
        
        frame = (frame + 1) % 8
        delay(0.05)
    pass

while(True):
    draw_animation(action)
    action = (action + 1) % 4

close_canvas()


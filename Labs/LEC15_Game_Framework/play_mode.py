import game_framework
from pico2d import *
import game_world
from boy import Boy
from grass import Grass
import ball_item


item_mode = False
selected_item = ball_item.DEFAULT
item_select_image = None
SCREEN_CENTER_X = 400
SCREEN_CENTER_Y = 300
ITEM_KEYS = {
    SDLK_0: ball_item.NONE,
    SDLK_1: ball_item.SMALL_BALL,
    SDLK_2: ball_item.BIG_BALL,
}


def select_item(key):
    return ITEM_KEYS.get(key)


def reset_item_selection():
    global item_mode, selected_item
    item_mode = False
    selected_item = ball_item.DEFAULT


def handle_events():
    global item_mode, selected_item

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_mode = not item_mode
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode
            game_framework.push_mode(pause_mode)
        elif item_mode and event.type == SDL_KEYDOWN:
            item = select_item(event.key)
            if item is not None and ball_item.is_selectable(item):
                selected_item = item
        elif not item_mode:
            boy.handle_event(event, selected_item)

def init():
    global boy, item_mode, selected_item, item_select_image

    reset_item_selection()
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)
    item_select_image = load_image('item_select.png')

def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    if item_mode:
        item_select_image.draw(SCREEN_CENTER_X, SCREEN_CENTER_Y)
    update_canvas()

def finish():
    game_world.clear()


def pause():
    pass


def resume():
    pass

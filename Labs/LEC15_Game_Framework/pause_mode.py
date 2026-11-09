import game_framework
from pico2d import *
import play_mode


def init():
    pass


def finish():
    pass


def update():
    pass


def render():
    play_mode.render()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()

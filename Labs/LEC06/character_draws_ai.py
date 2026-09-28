from pico2d import *


def draw_character(x, y):
	clear_canvas()
	character.draw(x, y)
	update_canvas()
	delay(0.02)


open_canvas(800, 600)
character = load_image('character.png')

close_canvas()

import math
from pico2d import *


def draw_character(x, y):
	clear_canvas()
	character.draw(x, y)
	update_canvas()
	delay(0.02)


def move_circle():
	for degree in range(0, 360, 5):
		theta = math.radians(degree)
		x = 400 + 200 * math.cos(theta)
		y = 300 + 200 * math.sin(theta)
		draw_character(x, y)


def move_rectangle_top():
	for x in range(50, 751, 10):
		draw_character(x, 550)


def move_rectangle_right():
	for y in range(550, 49, -10):
		draw_character(750, y)


def move_rectangle_bottom():
	for x in range(750, 49, -10):
		draw_character(x, 50)


def move_rectangle_left():
	for y in range(50, 551, 10):
		draw_character(50, y)


def move_rectangle():
	move_rectangle_top()
	move_rectangle_right()
	move_rectangle_bottom()
	move_rectangle_left()


open_canvas(800, 600)
character = load_image('character.png')

close_canvas()

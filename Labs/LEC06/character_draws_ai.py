import math
from pico2d import *


WIDTH = 800
HEIGHT = 600
GROUND_Y = 30
MOVE_SPEED = 3
FRAME_DELAY = 0.01


def draw_frame(x, y):
	clear_canvas()
	grass.draw(WIDTH // 2, GROUND_Y)
	character.draw(x, y)
	update_canvas()
	delay(FRAME_DELAY)


def move_to(start_x, start_y, end_x, end_y):
	distance = math.hypot(end_x - start_x, end_y - start_y)
	steps = max(1, int(distance / MOVE_SPEED))

	for step in range(steps):
		progress = step / steps
		x = start_x + (end_x - start_x) * progress
		y = start_y + (end_y - start_y) * progress
		draw_frame(x, y)

	draw_frame(end_x, end_y)


def move_circle():
	center_x = WIDTH / 2
	center_y = 300
	radius = 200
	angle = 0
	angle_step = 0.02

	while angle < 2 * math.pi:
		x = center_x + radius * math.cos(angle)
		y = center_y + radius * math.sin(angle)
		draw_frame(x, y)
		angle += angle_step


def move_rectangle():
	left = 50
	right = WIDTH - 50
	bottom = 100
	top = HEIGHT - 100

	move_to(left, bottom, right, bottom)
	move_to(right, bottom, right, top)
	move_to(right, top, left, top)
	move_to(left, top, left, bottom)


def move_triangle():
	left = 50
	right = WIDTH - 50
	bottom = 100
	top = HEIGHT - 100
	center = WIDTH / 2

	move_to(left, bottom, right, bottom)
	move_to(right, bottom, center, top)
	move_to(center, top, left, bottom)


open_canvas(WIDTH, HEIGHT)
grass = load_image('grass.png')
character = load_image('character.png')

while True:
	move_circle()
	move_rectangle()
	move_triangle()

close_canvas()

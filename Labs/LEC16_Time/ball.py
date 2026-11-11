from pico2d import get_canvas_width, load_image

import game_world
import game_framework

LAUNCH_SPEED_X = 300
LAUNCH_SPEED_Y = 300
GRAVITY = 9.8 * (10.0 / 0.3)
GROUND_Y = 40


class Ball:
    images = {}

    def __init__(self, x, y, velocity_x, velocity_y=0, ball_type=1):
        if isinstance(velocity_x, tuple):
            velocity_x, velocity_y = velocity_x

        if ball_type not in Ball.images:
            Ball.images[ball_type] = load_image(
                'ball21x21.png' if ball_type == 1 else 'ball41x41.png')
        self.image = Ball.images[ball_type]
        self.x, self.y = x, y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self):
        self.x += self.velocity_x * game_framework.frame_time
        self.y += self.velocity_y * game_framework.frame_time
        self.velocity_y -= GRAVITY * game_framework.frame_time

        if self.y <= GROUND_Y:
            self.y = GROUND_Y
            self.velocity_x = 0
            self.velocity_y = 0
            game_world.remove_object(self)
            return

        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)


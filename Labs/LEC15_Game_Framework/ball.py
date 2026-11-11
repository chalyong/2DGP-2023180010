from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    SMALL_IMAGE_PATH = 'ball21x21.png'
    BIG_IMAGE_PATH = 'ball41x41.png'
    images = {}

    @classmethod
    def load_sprite(cls, image_path):
        if image_path not in cls.images:
            cls.images[image_path] = load_image(image_path)
        return cls.images[image_path]

    def __init__(self, x, y, velocity, image_path=SMALL_IMAGE_PATH):
        self.x, self.y = x, y
        self.velocity = velocity
        self.image = Ball.load_sprite(image_path)

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)

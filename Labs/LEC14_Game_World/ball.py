from pico2d import get_canvas_width, load_image


class Ball:
    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.direction = direction
        self.speed = 10
        self.image = load_image('ball41x41.png')

    def update(self):
        self.x += self.direction * self.speed
        if self.x < -21 or self.x > get_canvas_width() + 21:
            return True
        return False

    def draw(self):
        self.image.draw(self.x, self.y)

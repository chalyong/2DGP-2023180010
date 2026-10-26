from pico2d import load_image
from transitions import Machine

class Boy:
    IDLE = 'IDLE'

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')
        self.state: str = self.IDLE
        self.state_machine = Machine(
            model=self,
            states=[self.IDLE],
            initial=self.IDLE,
            auto_transitions=False,
        )
        self.state_machine.add_transition(
            trigger='stay_idle',
            source=self.IDLE,
            dest=self.IDLE,
        )

    def update(self):
        if self.state == self.IDLE:
            self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.state == self.IDLE:
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

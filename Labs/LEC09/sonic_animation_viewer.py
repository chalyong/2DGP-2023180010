# -*- coding: utf-8 -*-
# LEC09 - sonic 스프라이트 애니메이션 뷰어
from pico2d import *

CANVAS_W, CANVAS_H = 800, 600


def handle_events():
    """창 닫기 이벤트가 발생하면 False 를 반환한다."""
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
    return True


def main():
    open_canvas(CANVAS_W, CANVAS_H)

    running = True
    while running:
        delay(0.1)
        running = handle_events()

    close_canvas()


main()

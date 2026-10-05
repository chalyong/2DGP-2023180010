# -*- coding: utf-8 -*-
# LEC09 - sonic 스프라이트 애니메이션 뷰어
from pico2d import *

CANVAS_W, CANVAS_H = 800, 600


def main():
    open_canvas(CANVAS_W, CANVAS_H)

    while True:
        delay(0.1)

    close_canvas()


main()

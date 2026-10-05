# -*- coding: utf-8 -*-
# LEC09 - sonic 스프라이트 애니메이션 뷰어
from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2

SPRITE_SHEET = 'sonic-sprite.png'


def handle_events():
    """창 닫기 이벤트가 발생하면 False 를 반환한다."""
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
    return True


def draw_frame(sheet, frame, dx=CENTER_X, dy=CENTER_Y, scale=1):
    """frame = (sx, sy, sw, sh) 좌표의 프레임을 화면 (dx, dy)에 그린다."""
    sx, sy, sw, sh = frame
    sheet.clip_draw(sx, sy, sw, sh, dx, dy, int(sw * scale), int(sh * scale))


def main():
    open_canvas(CANVAS_W, CANVAS_H)
    sheet = load_image(SPRITE_SHEET)

    running = True
    while running:
        clear_canvas()
        draw_frame(sheet, (2, 447, 25, 39))
        update_canvas()
        delay(0.1)
        running = handle_events()

    close_canvas()


main()

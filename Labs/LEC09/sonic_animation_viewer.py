# -*- coding: utf-8 -*-
# LEC09 - sonic 스프라이트 애니메이션 뷰어
from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2

SPRITE_SHEET = 'sonic-sprite.png'

# 동작 12개의 재생 순서 (시트 순서, 행8·행10 끝 분리 포함)
ANIMATION_ORDER = [f'anim{i}' for i in range(1, 13)]

# 동작별 프레임 좌표 테이블: 프레임 = (sx, sy, sw, sh), 이미지 하단 기준
ANIMATIONS = {
    'anim1': [
        (2, 447, 25, 39), (32, 447, 22, 38), (59, 447, 27, 39),
        (86, 447, 27, 38), (118, 447, 27, 38), (150, 447, 27, 38),
        (182, 447, 27, 38), (209, 448, 28, 38), (237, 448, 29, 38),
        (270, 448, 24, 32), (303, 448, 28, 26),
    ],
    'anim2': [
        (9, 408, 25, 37), (37, 408, 26, 37), (65, 408, 30, 37),
        (97, 408, 37, 37), (135, 410, 32, 35), (170, 408, 31, 38),
        (206, 408, 26, 38), (238, 408, 24, 37), (263, 408, 29, 37),
        (295, 408, 36, 37), (334, 409, 32, 36), (370, 408, 29, 38),
    ],
    'anim3': [
        (1, 361, 33, 40), (39, 362, 35, 39), (89, 362, 35, 38),
        (131, 362, 33, 42), (181, 362, 34, 41), (228, 363, 33, 40),
    ],
    'anim4': [
        (1, 326, 29, 30), (36, 327, 28, 31), (67, 327, 30, 29),
        (98, 327, 31, 29), (131, 327, 29, 30), (162, 326, 29, 31),
        (193, 326, 30, 29), (230, 326, 31, 29), (268, 325, 30, 30),
    ],
    'anim5': [
        (1, 292, 30, 27), (36, 292, 29, 27), (70, 292, 29, 27),
        (105, 292, 29, 27), (139, 292, 29, 27), (174, 292, 29, 27),
    ],
    'anim6': [
        (1, 251, 28, 35), (36, 251, 30, 35), (74, 251, 31, 35),
        (111, 251, 31, 36), (149, 251, 30, 35), (186, 251, 31, 36),
    ],
    'anim7': [
        (1, 207, 28, 35), (36, 207, 30, 35), (72, 208, 39, 31),
        (123, 208, 39, 32), (172, 208, 39, 31), (218, 208, 38, 32),
    ],
    'anim8': [],
    'anim9': [],
    'anim10': [],
    'anim11': [],
    'anim12': [],
}


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
        frames = ANIMATIONS[ANIMATION_ORDER[0]]
        if frames:
            draw_frame(sheet, frames[0])
        update_canvas()
        delay(0.1)
        running = handle_events()

    close_canvas()


main()

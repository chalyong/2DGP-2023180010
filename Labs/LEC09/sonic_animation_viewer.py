# -*- coding: utf-8 -*-
"""LEC09 - sonic 스프라이트 애니메이션 뷰어

sonic-sprite.png 의 동작 12개를 순서대로 재생한다.
동작 하나당 5회 반복 후 1초 쉬고 다음 동작으로 넘어가며,
마지막 동작 이후 처음부터 무한 반복한다.
창 닫기로 종료한다.
"""
import math
import time

from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2

SPRITE_SHEET = 'sonic-sprite.png'

FPS = 10  # 프레임 전환 속도
REPEAT = 5  # 동작 하나당 반복 횟수
PAUSE_TIME = 1.0  # 동작 사이 대기 시간(초)

# 수평 이동 동작 (걷기/구르기/달리기): 이름 -> 초당 이동 픽셀
MOVE_LR_ANIMS = {
    'anim2': 120,   # 걷기 (2행)
    'anim4': 220,   # 구르기1 (4행)
    'anim5': 220,   # 구르기2 (5행)
    'anim6': 320,   # 달리기1 (6행)
    'anim7': 320,   # 달리기2 (7행)
}
MOVE_MARGIN = 80  # 화면 밖 기준 여유 폭(px)

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
    'anim8': [
        (1, 154, 24, 44), (33, 154, 24, 44), (65, 154, 20, 44),
        (90, 155, 25, 43), (119, 155, 25, 43), (149, 154, 20, 44),
    ],
    'anim9': [
        (1, 109, 26, 37), (31, 110, 31, 36), (64, 110, 31, 36),
        (99, 110, 33, 37), (136, 110, 32, 36), (176, 110, 33, 36),
        (217, 110, 33, 36), (254, 111, 33, 36),
    ],
    'anim10': [
        (6, 56, 34, 40), (49, 56, 34, 43),
    ],
    'anim11': [
        (184, 156, 40, 28), (232, 157, 39, 27),
    ],
    'anim12': [
        (96, 59, 23, 39), (125, 59, 23, 39),
    ],
}

# 재생 순서: 정의된 순서 그대로 (anim1 -> anim12)
ANIMATION_ORDER = list(ANIMATIONS)


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


def move_lr_x(name, elapsed):
    """수평 이동 동작의 x. 왼쪽 밖 -> 오른쪽 밖으로 이동하고, 나가면 왼쪽에서 재등장한다."""
    span = CANVAS_W + 2 * MOVE_MARGIN
    return int((elapsed * MOVE_LR_ANIMS[name]) % span - MOVE_MARGIN)


def calc_scale():
    """가장 작은 프레임도 화면 높이의 절반 이상이 되도록 기본 배율을 구한 뒤 1/4로 줄인다."""
    min_h = min(sh for frames in ANIMATIONS.values() for _, _, _, sh in frames)
    return math.ceil((CANVAS_H / 2) / min_h) // 4


def calc_ground_y(scale):
    """프레임 높이가 달라도 흔들리지 않도록 바닥선을 정한다."""
    ref_h = max(sh for frames in ANIMATIONS.values() for _, _, _, sh in frames)
    return CENTER_Y + ref_h * scale // 2


def main():
    open_canvas(CANVAS_W, CANVAS_H)
    sheet = load_image(SPRITE_SHEET)
    scale = calc_scale()
    ground_y = calc_ground_y(scale)

    running = True
    anim_index = 0
    frame_index = 0
    repeat_count = 0
    pause_start = None  # 1초 대기 시작 시각 (미대기 상태)
    anim_start = time.time()  # 현재 동작 시작 시각 (이동 동작 위치 계산용)
    while running:
        clear_canvas()
        if pause_start is None:
            name = ANIMATION_ORDER[anim_index]
            frames = ANIMATIONS[name]
            if frames:
                sx, sy, sw, sh = frames[frame_index]
                # 바닥선 기준 정렬: 짧은 프레임도 발이 같은 높이에 오도록
                y = ground_y - sh * scale // 2
                x = CENTER_X
                if name in MOVE_LR_ANIMS:
                    x = move_lr_x(name, time.time() - anim_start)
                draw_frame(sheet, (sx, sy, sw, sh), dx=x, dy=y, scale=scale)
        update_canvas()
        delay(1.0 / FPS)

        if pause_start is not None:
            # 실시간 경과 시간 기준 -> delay 오차가 1초 대기에 누적되지 않음
            if time.time() - pause_start >= PAUSE_TIME:
                # 마지막 동작(anim12) 다음은 다시 anim1 -> 무한 반복
                anim_index = (anim_index + 1) % len(ANIMATION_ORDER)
                frame_index = 0
                repeat_count = 0
                pause_start = None
                anim_start = time.time()
        else:
            frame_index += 1
            if frame_index >= len(frames):
                frame_index = 0
                repeat_count += 1
                if repeat_count >= REPEAT:
                    repeat_count = 0
                    pause_start = time.time()
        running = handle_events()

    close_canvas()


if __name__ == '__main__':
    main()

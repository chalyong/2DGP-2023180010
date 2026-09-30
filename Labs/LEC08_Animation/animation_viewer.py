# -*- coding: utf-8 -*-
# LEC08 - 스프라이트 시트 애니메이션 뷰어
# character_atlas.png / character_atlas.json 을 이용한 애니메이션 재생기
# 2023180010
import json
import math

from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2

ANIM_ORDER = ['idle', 'walk', 'run', 'jump', 'attack']
REPEAT = 5
PAUSE_TIME = 1.0
TICK = 1.0 / 60

open_canvas(CANVAS_W, CANVAS_H)

atlas = load_image('character_atlas.png')
with open('character_atlas.json', encoding='utf-8') as fp:
    META = json.load(fp)

ATLAS_W, ATLAS_H = META['atlas_size']
ANIMATIONS = META['animations']

# 가장 작은 프레임도 화면 높이의 절반 이상이 되도록 스케일을 정한다.
MIN_FRAME_H = min(f['h'] for a in ANIMATIONS.values() for f in a['frames'])
SCALE = math.ceil((CANVAS_H / 2) / MIN_FRAME_H)

# 프레임마다 높이가 다르기 때문에 clip_draw 의 '중심' 기준으로는 캐릭터가
# 위아래로 흔들린다. 기준 높이만큼을 바닥선(GROUND_Y)에 맞춰 그림 위치로 보정한다.
REF_H = max(f['h'] for a in ANIMATIONS.values() for f in a['frames'])
GROUND_Y = CENTER_Y + REF_H * SCALE // 2


def draw_frame(frame, x=CENTER_X, w=None, h=None):
    # clip_draw 의 7, 8 번째 인수는 화면에 그릴 실제 크기(확대)이다.
    w, h = frame['w'] * SCALE, frame['h'] * SCALE
    # 프레임 높이가 달라도 바닥선은 같도록 y 를 보정한다.
    y = GROUND_Y - h // 2
    # clip_draw 의 두 번째 인수는 이미지 '하단' 기준 좌표이고,
    # JSON 의 y 는 '상단' 기준이므로 ATLAS_H 로 변환해야 한다.
    left = frame['x']
    bottom = ATLAS_H - frame['y'] - frame['h']
    atlas.clip_draw(left, bottom, frame['w'], frame['h'], x, y, w, h)


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


order_index = 0
frame_index = 0
repeat_count = 0
paused = False
pause_timer = 0.0
running = True

while running:
    name = ANIM_ORDER[order_index]
    anim = ANIMATIONS[name]

    if paused:
        # 5회 반복을 마친 뒤 1초 동안 정지한다.
        clear_canvas()
        update_canvas()
        delay(TICK)
        pause_timer -= TICK
        if pause_timer <= 0:
            paused = False
            order_index = (order_index + 1) % len(ANIM_ORDER)
    else:
        clear_canvas()
        draw_frame(anim['frames'][frame_index])
        update_canvas()
        delay(1.0 / anim['fps'])

        # 애니메이션마다 프레임 수가 다르므로 count 로 비교한다.
        frame_index += 1
        if frame_index >= anim['count']:
            frame_index = 0
            repeat_count += 1
            if repeat_count >= REPEAT:
                repeat_count = 0
                paused = True
                pause_timer = PAUSE_TIME

    running = handle_events()

close_canvas()

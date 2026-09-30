# -*- coding: utf-8 -*-
# LEC08 - 스프라이트 시트 애니메이션 뷰어
# character_atlas.png / character_atlas.json 을 이용한 애니메이션 재생기
# 2023180010
import json
import math

from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2

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


def play_loop(name):
    """name 애니메이션을 무한 반복한다. False 를 반환하면 종료."""
    anim = ANIMATIONS[name]
    index = 0
    while True:
        clear_canvas()
        draw_frame(anim['frames'][index % anim['count']])
        update_canvas()
        delay(1.0 / anim['fps'])
        index += 1

        if not handle_events():
            return False


running = True
while running:
    running = play_loop('idle')

close_canvas()

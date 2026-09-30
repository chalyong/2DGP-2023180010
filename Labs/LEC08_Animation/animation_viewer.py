# -*- coding: utf-8 -*-
# LEC08 - 스프라이트 시트 애니메이션 뷰어
# character_atlas.png / character_atlas.json 을 이용한 애니메이션 재생기
# 2023180010
import json

from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2

open_canvas(CANVAS_W, CANVAS_H)

atlas = load_image('character_atlas.png')
with open('character_atlas.json', encoding='utf-8') as fp:
    META = json.load(fp)

ATLAS_W, ATLAS_H = META['atlas_size']
ANIMATIONS = META['animations']


def draw_frame(frame, x, y, w=None, h=None):
    # clip_draw 의 7, 8 번째 인수는 화면에 그릴 실제 크기(확대)이다.
    if w is None:
        w, h = frame['w'] * 2, frame['h'] * 2
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
        draw_frame(anim['frames'][index % anim['count']], CENTER_X, CENTER_Y)
        update_canvas()
        delay(1.0 / anim['fps'])
        index += 1

        if not handle_events():
            return False


running = True
while running:
    running = play_loop('idle')

close_canvas()

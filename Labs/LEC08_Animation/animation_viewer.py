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
    # clip_draw 의 두 번째 인수는 이미지 '하단' 기준 좌표이고,
    # JSON 의 y 는 '상단' 기준이므로 ATLAS_H 로 변환해야 한다.
    left = frame['x']
    bottom = ATLAS_H - frame['y'] - frame['h']
    atlas.clip_draw(left, bottom, frame['w'], frame['h'], x, y, w, h)


def play_once(name):
    """name 애니메이션의 모든 프레임을 순서대로 한 번씩 그린다."""
    anim = ANIMATIONS[name]
    for index in range(anim['count']):
        clear_canvas()
        draw_frame(anim['frames'][index], CENTER_X, CENTER_Y)
        update_canvas()


while True:
    play_once('idle')
    delay(0.1)

close_canvas()

# -*- coding: utf-8 -*-
"""
LEC08 - 스프라이트 시트 애니메이션 뷰어

- character_atlas.json 메타데이터에서 애니메이션별 fps 와 프레임 수를 읽는다.
- 프레임마다 크기가 다른 스프라이트 시트를 clip_draw 로 잘라 그린다.
- clip_draw 의 확대 인자로 캐릭터를 화면 높이의 절반 이상으로 표시한다.
- 각 애니메이션을 5회 반복한 뒤 1초 정지하고, 전체를 순서대로 무한 반복한다.
"""
import json
import math

from pico2d import *

CANVAS_W, CANVAS_H = 800, 600
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2

ATLAS_FILE = 'character_atlas.png'
META_FILE = 'character_atlas.json'

ANIM_ORDER = ['idle', 'walk', 'run', 'jump', 'attack']
REPEAT = 5
PAUSE_TIME = 1.0
TICK = 1.0 / 60


def load_assets():
    """스프라이트 시트 이미지와 메타데이터를 읽는다."""
    image = load_image(ATLAS_FILE)
    with open(META_FILE, encoding='utf-8') as fp:
        meta = json.load(fp)
    return image, meta


def calc_scale(animations):
    """가장 작은 프레임도 화면 높이의 절반 이상이 되도록 스케일을 구한다."""
    min_h = min(f['h'] for a in animations.values() for f in a['frames'])
    return math.ceil((CANVAS_H / 2) / min_h)


def calc_ground_y(animations, scale):
    """프레임 높이가 달라도 흔들리지 않도록 바닥선을 정한다."""
    ref_h = max(f['h'] for a in animations.values() for f in a['frames'])
    return CENTER_Y + ref_h * scale // 2


def draw_frame(image, animations, atlas_h, scale, ground_y, name, index):
    """name 애니메이션의 index 프레임을 화면 중앙(바닥선 기준)에 그린다."""
    frame = animations[name]['frames'][index]
    # 7, 8 번째 인수는 화면에 그릴 실제 크기(확대)이다.
    w, h = frame['w'] * scale, frame['h'] * scale
    y = ground_y - h // 2
    # 두 번째 인수는 이미지 '하단' 기준, JSON 의 y 는 '상단' 기준이다.
    bottom = atlas_h - frame['y'] - frame['h']
    image.clip_draw(frame['x'], bottom, frame['w'], frame['h'], CENTER_X, y, w, h)


def handle_events():
    """종료 이벤트가 발생하면 False 를 반환한다."""
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


def main():
    open_canvas(CANVAS_W, CANVAS_H)

    image, meta = load_assets()
    animations = meta['animations']
    atlas_h = meta['atlas_size'][1]

    scale = calc_scale(animations)
    ground_y = calc_ground_y(animations, scale)

    order_index = 0
    frame_index = 0
    repeat_count = 0
    paused = False
    pause_timer = 0.0
    running = True

    while running:
        name = ANIM_ORDER[order_index]
        anim = animations[name]

        if paused:
            clear_canvas()
            update_canvas()
            delay(TICK)
            pause_timer -= TICK
            if pause_timer <= 0:
                paused = False
                order_index = (order_index + 1) % len(ANIM_ORDER)
        else:
            clear_canvas()
            draw_frame(image, animations, atlas_h, scale, ground_y,
                       name, frame_index)
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


main()

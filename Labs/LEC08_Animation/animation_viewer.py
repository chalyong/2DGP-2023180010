# -*- coding: utf-8 -*-
# LEC08 - 스프라이트 시트 애니메이션 뷰어
# character_atlas.png / character_atlas.json 을 이용한 애니메이션 재생기
# 2023180010
from pico2d import *

open_canvas(800, 600)

while True:
    clear_canvas()
    update_canvas()
    delay(0.1)

close_canvas()

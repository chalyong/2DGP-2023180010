NONE = 0
SMALL_BALL = 1
BIG_BALL = 2

DEFAULT = SMALL_BALL

IMAGE_PATHS = {
    SMALL_BALL: 'ball21x21.png',
    BIG_BALL: 'ball41x41.png',
}


def is_selectable(item):
    return item in (NONE, SMALL_BALL, BIG_BALL)

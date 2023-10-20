from PIL import ImageGrab
import numpy as up

__IS_WHITE = 1
__NOT_WHITE = 0


def check():
    screen = ImageGrab.grab(bbox=(0, 0, 1900, 1080))
    image_array = up.array(screen)
    color_array = up.mean(image_array, axis=(0, 1))

    if up.all(color_array >= 200):
        print("白屏")
        return __IS_WHITE
    else:
        print("非白屏")
        return __NOT_WHITE



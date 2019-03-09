import win32api
from win32con import *
from PIL import Image
import time
import core
SCREEN_WIDTH = win32api.GetSystemMetrics(0)
SCREEN_HEIGHT = win32api.GetSystemMetrics(1)


def get_revoled_xy(ox, oy):
    return ox * 65536 // SCREEN_WIDTH, oy * 65536 // SCREEN_HEIGHT


def press(force):
    x, y = get_revoled_xy(306, 618)
    win32api.mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(force / 10)
    win32api.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def restart():
    x, y = get_revoled_xy(193, 624)
    win32api.mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


while True:
    try:
        time.sleep(4)
        dis = core.snapshot()
        press(dis / 26)
        # Image.open('screenshot-2.png').show()
    except:
        raise Exception("over")
        # restart()

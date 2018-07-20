# coding=utf-8
from ctypes import *
import time

dd_dll = windll.LoadLibrary('./DD81200x64.64.dll')

# DD虚拟码，可以用DD内置函数转换。
vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302,
      'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308,
      'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408,
      '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211,
      '=': 212, 's': 402, ';': 410}
# 需要组合shift的按键。
vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7', '{': '[',
       '_': '-', '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}


def down_up(code):
    dd_dll.DD_key(vk[code], 1)
    dd_dll.DD_key(vk[code], 2)


def send_key(text):
    if not isinstance(text, str) or not isinstance(text, unicode):
        for key_name in text:
            if key_name.isupper():
                dd_dll.DD_key(500, 1)
                down_up(key_name.lower())
                dd_dll.DD_key(500, 2)

            elif key_name in '~!@#$%^&*()_+{}|:"<>?':
                dd_dll.DD_key(500, 1)
                down_up(vk2[key_name])
                dd_dll.DD_key(500, 2)
            else:
                down_up(key_name)
            time.sleep(0.2)
    else:
        raise ValueError("Wrong text instance {}".format(text))


if __name__ == "__main__":
    send_key("test")

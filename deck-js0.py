#!/usr/bin/env python
from pyjoystick.sdl2 import Key, Joystick, run_event_loop

def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def key_received(key):
    if key.keytype == Key.BUTTON:
        print('received', key, " ", key.value)
    # if key.value == Key.HAT_UP:
    #     print("hat up")
    # elif key.value == Key.HAT_DOWN:
    #     print("hat down")
    # if key.value == Key.HAT_LEFT:
    #     #do something
    # elif key.value == Key.HAT_UPLEFT:
    #     #do something
    # elif key.value == Key.HAT_DOWNLEFT:
    #     #do something
    # elif key.value == Key.HAT_RIGHT:
    #     #do something
    # elif key.value == Key.HAT_UPRIGHT:
    #     #do something
    # elif key.value == Key.HAT_DOWNRIGHT:
    #     #do something

run_event_loop(print_add, print_remove, key_received)
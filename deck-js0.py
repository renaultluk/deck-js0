#!/usr/bin/env python

import struct
from queue import Queue
from threading import Thread

infile_path = "/dev/input/js0"
EVENT_SIZE = struct.calcsize("LhBB")
file = open(infile_path, "rb")
event = file.read(EVENT_SIZE)

def event_emitter(out_q):
    global file
    global event
    while event:
        # print(struct.unpack("LhBB", event))
        # data = struct.unpack("LhBB", event)
        out_q.put(event)
        event = file.read(EVENT_SIZE)

def event_consumer(in_q):
    while True:
        event = in_q.get()
        (tv_msec,  value, type, number) = struct.unpack("LhBB", event)
        if type != 2 and type < 119:
            print(f"({value}, {type}, {number})")

q = Queue()
t1 = Thread(target=event_consumer, args=(q, ))
t2 = Thread(target=event_emitter, args=(q, ))
t1.start()
t2.start()
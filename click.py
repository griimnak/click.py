import os
import sys
import time
try:
    import pynput
except ImportError:
    exit("Please run 'pip install pynput'")

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
pos = None

print("Mouse over a target, and hit CTRL to lock mouse position.")


def click_loop(pos):
    interval = input("Please enter interval in seconds inbetween clicks: ")
    mouse.position = pos
    print('Using coords: {0}'.format(mouse.position))

    # press
    try:
        while True:
            mouse.position = pos
            mouse.press(pynput.mouse.Button.left)
            print("Click {0}".format(mouse.position))
            mouse.release(pynput.mouse.Button.left)
            time.sleep(int(interval))
    except KeyboardInterrupt:
        print("Goodbye")


def on_ctrl_key(key):
    # if CTRL is pressed only
    if key == pynput.keyboard.Key.ctrl_l:
        # stop listeneres
        listener.stop()
        # get mouse pos
        pos = mouse.position
        print('Mouse position locked: {0}'.format(pos))
        click_loop(pos)


with pynput.keyboard.Listener(on_press=on_ctrl_key) as listener:
    try:
        listener.join()
    except Exception as e:
        print('{0} was pressed'.format(e.args[0]))

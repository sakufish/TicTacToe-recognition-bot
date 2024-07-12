import keyboard
import time
import random

def hold_keys(duration):

    keyboard.press('w')
    if random.choice([1,2]) == 1:
        keyboard.press('space')
    time.sleep(duration)
    keyboard.release('w')
    keyboard.release('space')
    time.sleep(0.5)
    keyboard.press('s')
    time.sleep(duration)
    keyboard.release('s')


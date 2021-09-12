import pyautogui
import random
import time
import pydirectinput


def rt():

    return random.randint(1, 100)


def rt2():

    return random.randint(1, 55)


def rt3():

    return random.randint(1, 10)


def failsafe():
    return time.sleep(rt3())


def movemouse():

    # pyautogui.move(rt(), rt2(), duration=rt3())
    pydirectinput.move(rt(), rt2(), duration=rt3())
    failsafe()


#  def drag(x1, y1, x2, y2, duration, rate):
#     steps = int(duration / rate)
#     dx = (x2 - x1) / steps
#     dy = (y2 - y1) / steps
#     startTime = time.time()
#     lagCount = 0
#     for i in range(steps):
#         pydirectinput.move(int(x1 + i * dx), int(y1 + i * dy))
#         try:
#             time.sleep(rate * (i + 1) + startTime - time.time())
#         except ValueError:
#             lagCount += 1
#     failsafe()
#     print(steps, lagCount)


while True:
    movemouse()
    # drag(rt(), rt(), rt2(), rt2(), rt3(), 0.00001)

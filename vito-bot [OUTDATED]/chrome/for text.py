# for chrome

from random import randint
import pyautogui
import webbrowser
import time
import keyboard


def open_browser():
    f = open("profile.txt", "r")
    ch = f.readline()
    webbrowser.open(ch)
    f.close
    time.sleep(5)


def steps():
    time.sleep(1)
    if pyautogui.locateOnScreen('post.png') != None:
        xy = pyautogui.locateOnScreen('post.png')
    else:
        xy = pyautogui.locateOnScreen('night_post.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)

    if pyautogui.locateOnScreen('hap.png') != None:
        xy = pyautogui.locateOnScreen('hap.png')
    else:
        xy = pyautogui.locateOnScreen('night_hap.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)

    pyautogui.write(str(i), interval=0.25)
    time.sleep(1)

    if pyautogui.locateOnScreen('share.png') != None:
        xy = pyautogui.locateOnScreen('share.png')
    else:
        xy = pyautogui.locateOnScreen('night_share.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()


def refresh():
    xy = pyautogui.locateOnScreen('ref.png')
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2.5)


def er500():
    time.sleep(1.5)
    if pyautogui.locateOnScreen('err.png') != None:
        refresh()
        return True
    else:
        return False


# pp
c = 0
open_browser()
while keyboard.is_pressed("q") == False:
    i = randint(00000000, 99999999)
    steps()
    c = c+1
    if er500() == True:
        c = 1
    if c == 4:
        c = 1
        refresh()

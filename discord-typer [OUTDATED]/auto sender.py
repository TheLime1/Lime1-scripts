# by lime
from random import randint
import pyautogui
import time
import keyboard


def open_discord():

    # change dis
    path = ("C:\\Users\\everp\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe")

    pyautogui.keyDown("win")
    pyautogui.press("r")
    pyautogui.keyUp("win")
    keyboard.write(path)
    pyautogui.press("enter")
    time.sleep(5)
    xy = pyautogui.locateOnScreen('sbs.png')  # change dis imgs
    time.sleep(0.5)
    pyautogui.moveTo(xy)
    time.sleep(0.5)
    pyautogui.click()


def write_msg():
    xy = pyautogui.locateOnScreen('msgbox.png')
    pyautogui.moveTo(xy)
    pyautogui.click()
    while True:
        sec = randint(11, 250)
        msg = randint(0, len(listl)-1)
        time.sleep(sec)
        pyautogui.write(listToString(listl[msg]), interval=0.25)
        pyautogui.press("enter")


def get_list():
    global listl
    with open('msg.txt', 'r') as f:
        listl = []
        for line in f:
            strip_lines = line.strip()
            listli = strip_lines.split()
            m = listl.append(listli)
        print(listl)


def listToString(s):
    str1 = " "
    return (str1.join(s))


# pp
open_discord()
get_list()
write_msg()

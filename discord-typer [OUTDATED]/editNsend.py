# by lime
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


def write_msg(typ):
    xy = pyautogui.locateOnScreen('msgbox.png')
    pyautogui.moveTo(xy)
    pyautogui.click()
    i = 0
    if typ == "txt":
        while i < (len(listl)-1):
            pyautogui.write(listToString(listl[i]), interval=0.07)
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.press("up")
            time.sleep(0.5)
            pyautogui.keyDown("ctrl")
            pyautogui.press("a")
            pyautogui.keyUp("ctrl")
            i = i+1
            if i == len(listl)-1:
                i = 0
    if typ == "num":
        while True:
            pyautogui.write(str(i), interval=0.07)
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.press("up")
            time.sleep(0.5)
            pyautogui.keyDown("ctrl")
            pyautogui.press("a")
            pyautogui.keyUp("ctrl")
            i = i+1


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
write_msg("txt")  # change to num or txt

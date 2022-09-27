import logging
import pyautogui
import os
import time

os.startfile('chrome.exe')
time.sleep(1)
pyautogui.press('F6')
time.sleep(3)
pyautogui.write('github.com/login')
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(1000,100)



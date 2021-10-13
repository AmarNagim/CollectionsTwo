from pynput.keyboard import Key, Controller
import os           
import pyautogui
import time
import keyboard

path = os.getcwd() and __file__
file = "boodschappenlijstje"                     # input name of program 


os.system(f'start cmd {path}')
time.sleep(0.1)
keyboard.write(f'py {file}.py')
pyautogui.press('enter')
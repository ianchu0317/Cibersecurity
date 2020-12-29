#The only problem is the pyautogui Failsafe error will show up bc i dont know how to disable it -ian
import pyautogui
from time import sleep

pyautogui.FAILSAFE = False

pyautogui.hotkey("win", "r")
pyautogui.typewrite("powershell")
pyautogui.press("enter")
sleep(1)
pyautogui.typewrite("powershell start-process powershell -Verb runas")
pyautogui.press("enter")
sleep(2)
pyautogui.hotkey("left")
pyautogui.hotkey("enter")
sleep(1)
pyautogui.typewrite("Set-MpPreference -DisableRealtimeMonitoring $false")
pyautogui.press("enter")

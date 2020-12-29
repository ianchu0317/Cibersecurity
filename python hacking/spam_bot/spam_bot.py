from pynput.keyboard import Key, Controller
from time import sleep

c = Controller()
sleep(5)
with open("spam_text.txt", "a") as file:
    for x in range (500000):
        file.write("cri cri")
        file.write("\n")

with open("spam_text.txt", "r") as file:
    for x in range(500000):
        spam = file.read()
        c.type(spam)
        c.press(Key.enter)
        c.release(Key.enter)
        sleep(3)

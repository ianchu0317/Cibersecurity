import pyautogui, os, time
from sys import platform

def scr():
    try:
        sc = pyautogui.screenshot()
        path = os.listdir()
        #print(path) This is an error
        save_path = os.getcwd()
        t = time.asctime()
        if "save" in path:
            sc.save(save_path + f"/save/{t}.png")
        else:
            os.makedir("save")
            sc.save(save_path + f"/save/{t}.png")
    except NotImplementedError:
        if platform == "linux" or platform=="linux2":
            os.system("sudo apt-get install scrot")
            scr()

if __name__=="__main__":
    scr()
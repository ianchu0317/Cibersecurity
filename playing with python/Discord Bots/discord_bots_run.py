import threading
from os import system

def run_anashex():
    system("python discord_bot/discord_bot.py")

def run_herculanus():
    system("python herculanus/herculanus.py")

def run_pancracius():
    system("python pancracius/pancracius.py")

if __name__ == "__main__":
    anashex = threading.Thread(target=run_anashex)
    herculanus = threading.Thread(target=run_herculanus)
    pancracius = threading.Thread(target=run_pancracius)
    try:
        anashex.start()
        herculanus.start()
        pancracius.start()
    except KeyboardInterrupt:
        pass
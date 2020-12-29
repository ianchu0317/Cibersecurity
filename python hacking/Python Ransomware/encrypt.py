from cryptography.fernet import Fernet
import os 

def generate_key(): 
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file: 
		key_file.write(key)

def load_key(): 
	return open("key.key", "rb").read()

def encrypt(item, key):
	f = Fernet(key)
	with open(item, "rb") as file:
		content = file.read()
	encrypted_data = f.encrypt(content)
	with open(item, "wb") as file:
		file.write(encrypted_data)
 

if __name__ == "__main__":
	path = "C:\\Users\\ianch\\Desktop\\prueba"
	items = os.listdir(path)
#full_path = [path + "\\" + str(for item in items)]
	
	generate_key()
	
	key = load_key()
	for item in items:
		encrypt(item, key)
	

	#with open()
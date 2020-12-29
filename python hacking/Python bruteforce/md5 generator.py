import hashlib
encrypt = input("Insert word for encrypt: ")
encrypted = hashlib.md5(encrypt.encode("utf-8")).hexdigest()

with open("generated.txt", "w") as file: 
	file.write(str(encrypted))


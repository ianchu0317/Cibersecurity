#!/usr/bin/env python3 
cipher = input("[+]Enter your string: ").strip()


decrypt = ""
a = "abcdefghijklmnopqrstuvwxyz".strip()

for key in range(26+1):
	decrypt = ""
	for letter in cipher:
		if letter in a:
			decrypt += a[((a.find(letter))-key)]		
		else:
			break 
	print(f"{key}:{decrypt}")

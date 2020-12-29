import random
from string import ascii_letters, digits, punctuation

def generate_():
    global passw
    char = characters[random.randint(0, len(characters)-1)]
    if char in seed:
        generate_()
    else:
        seed.append(char)
        passw += char

if __name__== "__main__":
    passw, seed, characters = "", [], ascii_letters + digits + punctuation
    for i in range(10):
        generate_()
    print(passw)
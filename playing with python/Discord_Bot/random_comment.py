from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from nltk import sent_tokenize
from random import choice

# Random Messages Input
bruh = ["Bruh", "bruh", "bah", "aaaaaa"]
troll = ["xD", "XD", "JAJAJA", "jajaja", "jaja", "jajajajaja", "haha"]
Saludo = ["Hello", "Hola", "Hi", "hola", "hi", "yo", "hi"]
goodbye = ["Chau", "Bye", "Great"]

#Random Messages output
troll_response = [":poop:", ":woozy_face:", "Stupid", "Not funny"]
bruh_response = [":poop:", ":woozy_face:", "Stupid", "Not funny"]
saludo_response = ["Hi", "Hola", "Hey you", "Hi", "Hello, how are you ?", "Hola, cómo estás ?"]
goodbye_response = ["Chau, no te extraño", "Bye, I won't miss you", "Hasta nunca", "See you never"]

#Random Class
class Random:
    def __init__(self, msg):
        self.stemmer = SnowballStemmer("english")
        self.msg = msg
    #check the input, and give the output
    def check_(self, msg):
        msg = word_tokenize(msg)
        for word in msg:
            if word in bruh:
                return choice(bruh_response)
            elif word in troll:
                return choice(troll_response)
            elif word in Saludo:
                return choice(saludo_response)
            elif word in goodbye:
                return choice(goodbye_response)

    #Return the output
    def random_return(self):
        msg = word_tokenize(self.msg)
        for word in msg:
            if word in bruh:
                return choice(bruh_response)
            elif word in troll:
                return choice(troll_response)
            elif word in Saludo:
                return choice(saludo_response)
            elif word in goodbye:
                return choice(goodbye_response)
if __name__ == "__main__":
    palabra = "hola como te va"
    test = Random(palabra)
    msg = test.random_return()
    print(msg)
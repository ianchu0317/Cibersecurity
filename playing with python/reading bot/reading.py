#We need to import some modules to work to
import os
from gtts import gTTS
from time import sleep

#This is a testing code
class testing:
    def print(self):
        print("This is a test")


class Reading:
    def __init__(self, texts, languaje, name):
        self.text = texts
        self.lan = languaje
        self.name = name
        self.read = gTTS


    def generate(self):
        try:
            with open(self.text, "rb") as file:
                text = file.read()

            self.read(text = str(text), lang= str(self.lan))
            self.name = str(str(self.name)+".mp3")
            #name = input ("[+] Enter a name to the file: ")
            self.read.save("prueba.mp3")
        except ValueError:
            print("The given document is invalid: ")


class Languaje:
    def __init__(self, lang_def):
        pass
        self.lang_def = lang_def

    def main_lang(self):
        languaje_main = """
    Languaje main: 
    -1-   'af': 'Afrikaans',
    -2-    'ar': 'Arabic',
    -3-    'bn': 'Bengali',
    -4-    'bs': 'Bosnian',
    -5-    'ca': 'Catalan',
    -6-    'cs': 'Czech',
    -7-    'cy': 'Welsh',
    -8-    'da': 'Danish',
    -9-    'de': 'German',
    -10-    'el': 'Greek',
    -11-    'en': 'English',
    -12-    'eo': 'Esperanto',
    -13-    'es': 'Spanish',
    -14-    'et': 'Estonian',
    -15-    'fi': 'Finnish',
    -16-    'fr': 'French',
    -17-    'gu': 'Gujarati',
    -18-    'hi': 'Hindi',
    -19-    'hr': 'Croatian',
    -20-    'hu': 'Hungarian',
    -21-    'hy': 'Armenian',
    -22-    'id': 'Indonesian',
    -23-    'is': 'Icelandic',
    -24-    'it': 'Italian',
    -25-    'ja': 'Japanese',
    -26-    'jw': 'Javanese',
    -27-    'km': 'Khmer',
    -28-    'kn': 'Kannada',
    -29-    'ko': 'Korean',
    -30-    'la': 'Latin',
    -31-    'lv': 'Latvian',
    -32-    'mk': 'Macedonian',
    -33-    'ml': 'Malayalam',
    -34-    'mr': 'Marathi',
    -35-    'my': 'Myanmar (Burmese)',
    -36-    'ne': 'Nepali',
    -37-    'nl': 'Dutch',
    -38-    'no': 'Norwegian',
    -39-    'pl': 'Polish',
    -40-    'pt': 'Portuguese',
    -41-    'ro': 'Romanian',
    -42-    'ru': 'Russian',
    -43-    'si': 'Sinhala',
    -44-    'sk': 'Slovak',
    -45-    'sq': 'Albanian',
    -46-    'sr': 'Serbian',
    -47-    'su': 'Sundanese',
    -48-    'sv': 'Swedish',
    -49-    'sw': 'Swahili',
    -50-    'ta': 'Tamil',
    -51-    'te': 'Telugu',
    -52-    'th': 'Thai',
    -53-    'tl': 'Filipino',
    -54-    'tr': 'Turkish',
    -55-    'uk': 'Ukrainian',
    -56-    'ur': 'Urdu',
    -57-    'vi': 'Vietnamese',
    -58-    'zh-CN': 'Chinese'   
"""

        print(languaje_main)


    def select_languaje(self):
        lang = input("[+] Insert the number to choose the languaje (English default): ")
        if "," in lang:
            lang.split(",")
        elif " " in lang:
            lang.split(" ")
        elif "." in lang:
            lang.split(".")
        else:
            pass

        if lang == "1":
            self.lang_def = str("af")
        elif lang == "2":
            self.lang_def = str("ar")
        elif lang == "3":
            self.lang_def = str("bn")
        elif lang == "4":
            self.lang_def = str("bs")
        elif lang == "5":
            self.lang_def = str("ca")
        elif lang == "6":
            self.lang_def = str("cs")
        elif lang == "7":
            self.lang_def = str("cy")
        elif lang == "8":
            self.lang_def = str("da")
        elif lang == "9":
            self.lang_def = str("de")
        elif lang == "10":
            self.lang_def = str("el")
        elif lang == "11":
            self.lang_def = str("en")
        elif lang == "12":
            self.lang_def = str("eo")
        elif lang == "13":
            self.lang_def = str("es")
        elif lang == "14":
            self.lang_def = str("et")
        elif lang == "15":
            self.lang_def = str("fi")
        elif lang == "16":
            self.lang_def = str("gr")
        elif lang == "17":
            self.lang_def = str("gu")
        elif lang == "18":
            self.lang_def = str("hi")
        elif lang == "19":
            self.lang_def = str("hr")
        elif lang == "20":
            self.lang_def = str("hu")
        elif lang == "21":
            self.lang_def = str("hy")
        elif lang == "22":
            self.lang_def = str("id")
        elif lang == "23":
            self.lang_def = str("is")
        elif lang == "24":
            self.lang_def = str("it")
        elif lang == "25":
            self.lang_def = str("ja")
        elif lang == "26":
            self.lang_def = str("jw")
        elif lang == "27":
            self.lang_def = str("km")
        elif lang == "28":
            self.lang_def = str("kn")
        elif lang == "29":
            self.lang_def = str("ko")
        elif lang == "30":
            self.lang_def = str("la")
        elif lang == "31":
            self.lang_def = str("lv")
        elif lang == "32":
            self.lang_def = str("mk")
        elif lang == "33":
            self.lang_def = str("ml")
        elif lang == "34":
            self.lang_def = str("mr")
        elif lang == "35":
            self.lang_def = str("my")
        elif lang == "36":
            self.lang_def = str("ne")
        elif lang == "37":
            self.lang_def = str("nl")
        elif lang == "38":
            self.lang_def = str("no")
        elif lang == "39":
            self.lang_def = str("pl")
        elif lang == "40":
            self.lang_def = str("pt")
        elif lang == "41":
            self.lang_def = str("ro")
        elif lang == "42":
            self.lang_def = str("ru")
        elif lang == "43":
            self.lang_def = str("si")
        elif lang == "44":
            self.lang_def = str("sk")
        elif lang == "45":
            self.lang_def = str("sq")
        elif lang == "46":
            self.lang_def = str("sr")
        elif lang == "47":
            self.lang_def = str("su")
        elif lang == "48":
            self.lang_def = str("sv")
        elif lang == "49":
            self.lang_def = str("sw")
        elif lang == "50":
            self.lang_def = str("ta")
        elif lang == "51":
            self.lang_def = str("te")
        elif lang == "52":
            self.lang_def = str("th")
        elif lang == "53":
            self.lang_def = str("tl")
        elif lang == "54":
            self.lang_def = str("tr")
        elif lang == "55":
            self.lang_def = str("uk")
        elif lang == "56":
            self.lang_def = str("ur")
        elif lang == "57":
            self.lang_def = str("vi")
        elif lang == "58":
            self.lang_def = str("zh-CN")
        else:
            print("The selected languaje is not valid")
            print("Going to the menu")
            sleep(1)



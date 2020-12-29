#import speech_recognition as sr
from speech_recognition import Recognizer, Microphone
from pyttsx3 import init

def speak(text):
    engine.say(text)
    engine.runAndWait()

def execute(text):
    text = text.lower()
    if "hi" in text or "hey" in text:
        speak("Hi, how are you")
    elif "your name" in text:
        speak("My name is Flora")
    elif "who created you" in text:
        speak("I'm created by Ian. He is a pro")
    else:
        speak("I don't understand")
        pass
    listen()

def listen():
    #global sr
    print("listening...")
    try:
        with Microphone() as flora:
            command = listener.listen(flora)
            print("success")
            execute(listener.recognize_google(command))
    except:
        print("failed")
        speak("I don't understand, say it again")
        listen()


if __name__ == "__main__":
    engine = init()
    engine.setProperty('rate', 160)
    listener = Recognizer()

    while True:
        listen()
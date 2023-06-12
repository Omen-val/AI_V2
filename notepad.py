import pyttsx3
import speech_recognition as sr
from time import sleep
import os
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices [2].id)
engine.setProperty('rate', 190)

def speak(audio):
        engine.say(audio)
        print(f"ZAX: {audio}")
        engine.runAndWait()

# To Convert Voice to Text

def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source,0,8)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language='en-in')
            print(f"You: {query}")
        except Exception as e:
            return ""
        return query


def NotePad():
      
    speak("Please tell me what to write.")
    sleep(0.5)

    writes = takecommand()

    time = datetime.datetime.now().strftime("%H:%M")

    filename = str(time).replace(":", "-") + " -note.txt"

    with open(filename, "w") as file:
         file.write(writes)

    path_a = "E:\\Coding Project\\Python\\ZAX AI\\" + str(filename)
    path_b = "E:\\Coding Project\\Python\\ZAX AI\\Notes\\" + str(filename)

    os.rename(path_a, path_b)
    os.startfile(path_b)

NotePad()
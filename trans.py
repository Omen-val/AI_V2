    
import speech_recognition as sr
from googletrans import Translator
import pyttsx3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
        engine.say(audio)
        print(f"You: {audio}")
        engine.runAndWait()



def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source,0,8)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language='bn')
            
        except Exception as e:
            speak("Say that again please...")
        
        query = str(query).lower()
        return query


def Trans(Text):
        line = str(Text)
        translate = Translator()
        result = translate.translate(line)
        data = result.text
        return data



def Mic():
        query = takecommand()
        data = Trans(query)
        return data

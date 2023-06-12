import pyttsx3
import os
from pytube import YouTube

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices [2].id)
engine.setProperty('rate', 190)

def speak(audio):
        engine.say(audio)
        print(f"ZAX: {audio}")
        engine.runAndWait()



def YT(link):
        youtubeObj = YouTube(link)
        youtubeOBJ2 = youtubeObj.streams.get_highest_resolution()

        try:
              youtubeOBJ2.download()  
        except:
                speak("An error occured")

        speak("Download is Complete!")

mainlink = str(input("Enter the link: "))
YT(mainlink)

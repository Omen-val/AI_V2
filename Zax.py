import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import webbrowser
from requests import get
import wikipedia
import pywhatkit as pywt
import sys
import pyjokes
import requests
import instaloader
import time
import pyautogui
from pynput.keyboard import Key, Controller
import pywikihow
import speedtest_cli
import keyboard
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# for i in range(3):
#     a = input("Enter password to unlock ZAX:- ")
#     pw = "ZAX"
#     if (a==pw) :
#         print("WELCOME BACK SIR!")
#         break

#     elif (i==2 and a!=pw):
#         print("Please try again later.")
#         exit()

#     elif (a!=pw):
#         print("Try Again")

# from ZAXUI import playgif
# playgif


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

    




# Wish Function
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <=12:
        speak("Good Morning!")

    elif hour>12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm Zax, How may I help you?")

def multiply():
    try:
        speak("PLease Enter the first Number")
        a = int(input("Please Enter first the number: "))
        speak("PLease Enter the second Number")
        b = int(input("Please Enter the second number: "))
        product = a * b
        speak(f"The answer is {product}")

    except Exception as e:
        speak("Please Enter a number!")

def add():
    try:
        speak("PLease Enter the first Number")
        a = int(input("Please Enter the first number: "))
        speak("PLease Enter the second Number")
        b = int(input("Please Enter the second number: "))
        sum = a + b
        speak(f"The answer is {sum}")

    except Exception as e:
        speak("Please Enter a number!")



def minus():
    try:
        speak("Please Enter first number")
        a = int(input("Please Enter the first number: "))
        speak("Please Enter second number")
        b = int(input("Please Enter the second number: "))
        diff = a - b
        speak(f"The answer is {diff}")

    except Exception as e:
        speak("Please Enter a number!")


def devide():
    try:
        speak("Please Enter first number")
        a = int(input("Enter the first number: "))
        speak("Please Enter second number")
        b = int(input("Please Enter the second number: "))
        que = a / b
        speak(f"The division answer is {que}")

    except Exception as e:
        speak("Please Enter a number!")

ctrl = Controller()

def volumeup():
    for i in range(5):
        ctrl.press(Key.media_volume_up)
        ctrl.release(Key.media_volume_up)
        time.sleep(0.1)

def volumedown():
    for i in range(5):
        ctrl.press(Key.media_volume_down)
        ctrl.release(Key.media_volume_down)
        time.sleep(0.1)


def OpenApp():
            speak("Please tell me the name of the software")
            query = takecommand().lower()
            App = query.replace("start", "")
            App = query.replace("zax", "")
            pyautogui.press('win')
            time.sleep(1)
            keyboard.write(App)
            time.sleep(0.5)
            keyboard.press('enter')
            time.sleep(3)
            speak("Programm Started")
            return True



def TakeBD():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source,0,8)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language='bn')
            print(f"You: {query}")
        except Exception as e:
            speak("Say that again please...")
            return "None"
        return query


def Trans():
    speak("Tell me the line")
    line = TakeBD()
    trans = Translator()
    res = trans.translate(line)
    txt = res.text
    speak(txt)


def WakeUp():
    print("PLEASE SAY [WAKE UP] to start me...")
    while True:
        permit = takecommand().lower()
        if 'wake up' in permit:
            TaskExe()
        elif 'sleep' in permit:
                sys.exit()

def Music():
    speak("What is the name of the song")
    Musicname = takecommand().lower()

    if 'dandelions' in Musicname:
        os.startfile("C:\\Users\\IT BD\\Music\\Dandelions.mp3")

    elif 'faded' in Musicname:
        os.startfile("C:\\Users\\IT BD\\Music\\Faded.mp3")

    elif 'hall of fame' in Musicname:
        os.startfile("C:\\Users\\IT BD\\Music\\hall of fame.mp3")

    elif 'senorita' in Musicname:
        os.startfile("C:\\Users\\IT BD\\Music\\Senorita.mp3")

    elif 'mockingbird' in Musicname:
        os.startfile("C:\\Users\\IT BD\\Music\\Mocking.mp3")

    elif "shape of you" in Musicname:
        os.startfile("C:\\Users\\IT BD\\Music\\Shape of you.mp3")

    else:
        pywt.playonyt(Musicname)

def TaskExe():
    wish()

    while True:
        query = takecommand().lower()

        # Task Execution



        if 'open notepad' in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)

        elif 'multiply' in query:
                speak("Ok, Sir!")
                time.sleep(1)
                multiply()

        elif 'addition' in query:
            speak("Ok, Sir!")
            time.sleep(1)
            add()

        elif 'divide' in query or 'division' in query:
            speak("Ok, Sir!")
            time.sleep(1)
            devide()

        elif 'minus' in query:
            speak("Ok, Sir!")
            time.sleep(1)
            minus()

        elif 'close notepad' in query:
            speak("Closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'quit' in query:
            speak("Okay, call me anytime!")
            speak("Say [sleep] to permenantly exit")
            speak("And say [WAKE UP] to wake me up again.")
            break

        elif 'open word' in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016.lnk"
            os.startfile(path)

        elif 'start' in query:
            OpenApp()

        elif 'close word' in query:
            speak("Closing Word...")
            os.system("taskkill /f /im Word 2016.lnk")

        elif 'open command' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:

                ret, img = cap.read()
                cv2.imshow('Zax Cam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif 'open viber' in query:
            path = "C:\\Users\\IT BD\\AppData\\Local\\Viber\\Viber.exe"
            os.startfile(path)

        elif 'close viber' in query:
            speak("Closing Viber...")
            os.system("taskkill /f /im Viber.exe")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"Sir the time is {strTime}")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            query = query.replace("zax", "")
            query = query.replace("search", "")
            speak("This is what I found!")
            pywt.search(query)
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)

            except:
                speak("No speakable data found!")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'facebook' in query:
            webbrowser.open("https://facebook.com")

        elif 'google' in query:
            speak("What Should I search on google?")
            search = takecommand().lower()

            webbrowser.open(f"{search}")

        elif 'youtube search' in query or 'search on youtube' in query:
            speak("This is what I found")
            query = query.replace("youtube search", "")
            query = query.replace("zax", "")
            query = query.replace("search", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            time.sleep(3)
            speak("Done! Should I play the first video ?")
            sui = takecommand().lower()
            if 'yes' in sui or 'yeah' in sui:
                pywt.playonyt(query)

            else:
                pass

        elif 'pause' in query:
            pyautogui.press("k")
            speak("video paused")

        elif 'play' in query:
            pyautogui.press("k")
            speak("video played")

        elif 'mute' in query:
            pyautogui.press("m")
            speak("video muted")

        elif 'volume up' in query:
            speak("Turning volume up")
            volumeup()

        elif 'volume down' in query:
            speak("Turning volume down")
            volumedown()

        elif 'forward' in query:
            pyautogui.press("l")
            speak("Video forwarded")

        elif 'rewind' in query:
            pyautogui.press("j")

        elif 'fullscreen' in query:
            pyautogui.press("f")

        elif 'remember' in query:
            rememberMsg = query.replace("remeber", "")
            rememberMsg = query.replace("zax", "")
            speak(f"You told me {rememberMsg}/n")
            remember = open("Remember.txt", "a")
            remember.write(rememberMsg)
            remember.close()

        elif 'brain' in query:
            remember = open("Remember.txt", "r")
            speak(f"You said to read {remember.read()}")

        elif 'power' in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Your battery is now at {percentage}%")
            if percentage>=75:
                speak("We enough power to continue")

            elif percentage>=30 and percentage <=75:
                speak("We should connect our system to charger")

            elif percentage<=20:
                speak("Please connect system to battery")

            elif percentage<=5:
                speak("Please connect your system to battery or your system will shutdown.")

        elif 'battery' in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Your battery is now at {percentage}%")
            if percentage>=75:
                speak("We enough power to continue")

            elif percentage>=30 and percentage <=75:
                speak("We should connect our system to charger")

            elif percentage<=20:
                speak("Please connect system to battery")

            elif percentage<=5:
                speak("Please connect your system to battery or your system will shutdown.")

        elif 'activate tutorial' in query:
            speak("Tutorial Mode is activated...")
            speak("Tell me what you want to know.")
            tut = takecommand().lower()
            max_results = 1
            tut_find = pywikihow.search_wikihow(tut, max_results)
            assert len (tut_find) ==1
            speak(tut_find[0].summary)


        elif 'wait' in query:
            speak("Ok sir!")
            time.sleep(4)
            speak("Are you done?")

            cmd = takecommand().lower()
            if 'yes' in cmd or 'yeah' in cmd:
                break
            else:
                time.sleep(4)

        elif 'translator' in query or 'translate' in query:
            Trans()

        elif 'board' in query:
            speak("Let's play Number Guessing game")
            from game import game
            game()

        elif 'bored' in query:
            speak("Let's play Number Guessing game")
            from game import game
            game()

        elif 'game' in query:
            speak("Let's play Number Guessing game")
            from game import game
            game()

        elif 'games' in query:
            speak("Let's play Number Guessing game")
            from game import game
            game()

        elif 'qr code' in query:
            from QRCODE import Generate

            speak("Tell me what convert into QR code")
            kk = input("Enter the link/text: ")
            Generate(kk)




    

        # elif 'focus mode' in query:
        #     a = int(input("Are you sure you want to enter FOCUS MODE [1 for YES / 2 for NO:- "))

        #     if (a==1):
        #         speak("ENTERING FOCUS MODE...")
        #         os.startfile("E:\\Coding Project\\Python\\ZAX AI\\FocusMode.py")
        #         exit()
        #     else:
        #             speak("Ok, quiting FOCUS MODE...")

        

        

        # elif 'send whatsapp message' in query:
        #     speak("What is the message?")
        #     msg = input("Enter your messege: ")
        #     pywt.sendwhatmsg("contact number of the person", msg, "enter the hour in number without the string", "enter the minute")
        #     #Note: you must enter the time minimum 3 minute ahead



        elif 'song' in query or 'music' in query:
            Music()

        elif 'no thanks' in query:
            speak("Ok, Bye!")
            speak("Say [sleep] to permenantly exit")
            speak("And say [WAKE UP] to wake me up again.")
            break

        elif 'call' in query:
            from whatsapp import WhatsAppcall

            speak("Tell me the name of the person")
            pers = takecommand().lower()

            WhatsAppcall(pers)

        elif 'message' in query:
            from whatsapp import WhatsAppMsg

            speak("Tell me the name of the person")
            pers = takecommand().lower()

            speak("Tell me the messege")
            msg = input("Enter the messege: ")

            WhatsAppMsg(pers, msg)

        elif 'video call' in query or 'video' in query:
            from whatsapp import WhatsAppVideo

            speak("Tell me the name of the person")
            pers = takecommand().lower()
            WhatsAppVideo(pers)

        elif 'chat' in query:
            from whatsapp import WhatsAppChat
            speak("Tell me the name of the person")
            pers = takecommand().lower()
            WhatsAppChat(pers)


        elif 'new window' in query:
            keyboard.press_and_release("ctrl + shift + n")

        elif 'tab' in query:
            keyboard.press_and_release("ctrl + t")

        elif 'history' in query:
            keyboard.press_and_release("ctrl + h")

        elif 'internet speed' in query:
            speak("Checking your internet speed...")
            import speedtest
            speed = speedtest.Speedtest()
            up = speed.upload()/1048576
            dw = speed.download()/1048576
            speak(f"Your Download speed is {dw} Mbps and your upload speed is {up} Mbps.")

        elif 'note' in query or 'write' in query:
            from notepad import NotePad

            NotePad()


        elif 'you need a break' in query:
            speak("Ok, See you!")
            speak("Say [sleep] to permenantly exit")
            speak("And say [WAKE UP] to wake me up again.")
            break

        elif 'shutdown computer' in query:
            os.system("shutdown /s /t 5")

        elif 'restart computer' in query:
            os.system("shutdown /r /t 5")

        elif 'where are we' in query or 'where am i' in query or 'location' in query:
            speak("Wait Sir, Let me check..")
            try:
                ipAdrs = requests.get('https://api.ipify.org').text
                print(ipAdrs)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdrs+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir, I'm not sure but, we are in the {city} of country {country}")

            except Exception as e:
                speak("Sir, I was unble find our loction due to network issues.")
                pass


        elif 'my home' in query or 'house' in query:
            webbrowser.open("https://www.google.com/maps/place/Hitech+Multicare+Hospital+ltd/@23.7885944,90.3878873,17.67z/data=!4m15!1m8!3m7!1s0x3755c73cfb37631d:0x749601cd45f0c3fd!2sKachukhet,+Dhaka!3b1!8m2!3d23.7940289!4d90.3901397!16s%2Fg%2F1v41ytq7!3m5!1s0x3755c738c7307319:0x4ff18db7d2a08b5f!8m2!3d23.7881492!4d90.3881544!16s%2Fg%2F11rrzd0_v!5m1!1e1")

        
        elif 'instagram profile' in query or 'insta pfp' in query:
            speak("Please enter the Instagram Profile name correctly!")
            name = input("Enter the Username:- ")
            webbrowser.open(f'https://instagram.com/{name}')
            speak(f"Sir, here is the instagram profile of {name}")
            time.sleep(5)
            speak("Would you like to download the profile picture of this user")
            answer = takecommand().lower()
            if 'yes' in answer or 'yeah' in answer:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("Sir, Profile Pic has been downloaded in our main folder")

            else:
                pass


        elif 'take a screenshot' in query or 'take screenshot' in query:
            speak("Please enter the name of the screenshot file.")
            screenstnm = input("Enter the Name: ")
            speak("Sir please hold still, I'm taking a screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{screenstnm}.jpg")
            speak("I'm done sir!")
            time.sleep(1.4)

        
        elif 'hide my file' in query or 'hide all file' in query or 'make it visible' in query:
            speak("Sir, Should I hide the files or make it visible")
            condition = takecommand().lower()

            if 'hide' in condition:
                os.system("attrib +h /s /d")
                speak("Sir, All files are now hidden")

            elif 'visible' in condition:
                os.system("attrib -h /s /d")
                speak("Sir, All files are now visible")

            elif 'leave it' in condition or 'leave for now' in condition:
                speak("Ok, Sir!")

# ---------CONVERSATION---------- #

        elif 'hello' in query:
                speak("Hi!, How are you?")

        elif 'how are you' in query:
                speak("Absolutely fine, Sir")
                speak("What about you")

        elif 'i am fine' in query:
            speak("That's Nice")

        elif 'joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)

        elif 'who are you' in query:
                speak("I'm your personal AI Assistant. My name is   Zax")

        elif 'thank you' in query or 'thanks' in query:
            speak("It's my pleasure sir!")

# ------CONVERSATION END--------- #



if __name__ =='__main__':
        # print("PLEASE SAY [WAKE UP] to start me...")
        # while True:
        #     permit = takecommand().lower()
        #     if 'wake up' in permit:
        #         TaskExe()
        #     elif 'sleep' in permit:
        #         sys.exit()
        from clap import Tester

        data = Tester()

        if "True-Mic" == data:
            time.sleep(3)
            WakeUp()


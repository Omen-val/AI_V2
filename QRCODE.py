import qrcode
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices [2].id)
engine.setProperty('rate', 190)

def speak(audio):
        engine.say(audio)
        print(f"ZAX: {audio}")
        engine.runAndWait()


def Generate(link):

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction= qrcode.constants.ERROR_CORRECT_L,
            box_size= 10,
            border=4
        )

        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrimage.png")
        speak("QR Code Generated!")

    
    except:
        speak("Something Went Wrong!")
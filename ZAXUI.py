from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()


root = Tk()
root.geometry("1000x520")
root.title("ZAX AI")

def playgif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("C:\\Users\\IT BD\\Pictures\\Saved Pictures\\Main.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i=0
    mixer.music.load("C:\\Users\\IT BD\\Pictures\\Saved Pictures\\ZAXedit2.mp3")
    mixer.music.play()

    for img in ImageSequence.Iterator(img):
        img = img.resize((1000, 520))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

playgif()
root.mainloop()
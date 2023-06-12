from pyautogui import click
import pyautogui
from keyboard import press
from time import sleep
from keyboard import write


def WhatsAppMsg(name, msg):
    pyautogui.press('win')
    sleep(0.5)
    write('WhatsApp')
    sleep(0.5)
    press('enter')
    sleep(5)
    click(x=258, y=151)
    sleep(1)

    write(name)
    sleep(1)
    click(x=409, y=219)
    sleep(1)
    click(x=929, y=993)
    sleep(1)
    write(msg)
    press('enter')


def WhatsAppcall(name):
    pyautogui.press('win')
    sleep(0.5)
    write('WhatsApp')
    sleep(0.5)
    press('enter')
    sleep(5)
    click(x=258, y=151)
    sleep(1)

    write(name)
    sleep(1)
    click(x=409, y=219)
    sleep(1)
    click(x=929, y=993)
    sleep(1)
    click(x=1765, y=96)


def WhatsAppChat(name):
    pyautogui.press('win')
    sleep(0.5)
    write('WhatsApp')
    sleep(0.5)
    press('enter')
    sleep(5)
    click(x=258, y=151)
    sleep(1)

    write(name)
    sleep(1)
    click(x=409, y=219)
    sleep(1)
    click(x=929, y=993)

def WhatsAppVideo(name):
    pyautogui.press('win')
    sleep(0.5)
    write('WhatsApp')
    sleep(0.5)
    press('enter')
    sleep(5)
    click(x=258, y=151)
    sleep(1)

    write(name)
    sleep(1)
    click(x=409, y=219)
    sleep(1)
    click(x=929, y=993)
    sleep(1)
    click(x=1557, y=279)
import win32com.client
import time
import pyautogui

outlook = win32com.client.Dispatch("Outlook.Application")
shell = win32com.client.Dispatch("WScript.Shell")


def Emailer(text, subject, recipient):

    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text

    mail.Display()
    # try and get past TITUS
    shell.AppActivate("Outlook")
    time.sleep(1)
    shell.SendKeys("{TAB}")
    pyautogui.press("alt")
    pyautogui.press("down")
    pyautogui.press("left",)
    pyautogui.press("enter")

    pyautogui.press("up")
    pyautogui.press("up")
    pyautogui.press("up")
    pyautogui.press("enter")

    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")

    mail.Send()


Emailer('Hello Kempton', 'Test SUbject6', 'kempton.mooney@gmail.com')

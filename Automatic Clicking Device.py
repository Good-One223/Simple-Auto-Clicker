import mouse
import time
import keyboard
from tkinter import *

colour = "#FEFAE5"
time_to_sleep = 0.1

window = Tk()
window.geometry("400x400")
window.title("Automatic Clicking Device")
window.config(bg=colour)


def Click():
    time.sleep(5)
    while not keyboard.is_pressed("f12"):
        mouse.click("left")
        time.sleep(time_to_sleep)


def ChangeSpeed():
    global time_to_sleep
    time_to_sleep = Settings.get()
    try:
        time_to_sleep = float(Settings.get())
        ErrorText["text"] = ""
    except ValueError:
        ErrorText["text"] = "Invalid Time, Try Again"


Title = Label(window, text="Automatic Clicking Device", padx=50,
              pady=10, bg=colour, font=("", 20, "bold"))

HowTo = Label(
    window, text='Click button to start clicking after a 5 second delay,\npress "f12" to turn off', padx=50, pady=20, bg=colour, font=("", 12))

Clickbutton = Button(window, text="Start Automatic Clicking Device",
                     padx=50, pady=30, font=("", 12), command=Click)

SettingsLabel = Label(window, text="Time Between Clicks:",
                      padx=50, pady=10, font=("", 12), bg=colour)

Settings = Entry(window, width=10, justify="center")
Settings.insert(0, str(time_to_sleep))

Confirm = Button(window, text="Confirm Speed", padx=10,
                 pady=5, font=("", 10), command=ChangeSpeed)

ErrorText = Label(window, text="", padx=50,
                  pady=0, bg=colour, font=("", 12))

Title.pack()
HowTo.pack()
Clickbutton.pack()
SettingsLabel.pack()
Settings.pack()
Confirm.pack(pady=10)
ErrorText.pack()


window.mainloop()

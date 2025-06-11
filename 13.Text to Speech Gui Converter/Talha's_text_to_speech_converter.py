import tkinter as tk
from tkinter import *
import pyttsx3

engine = pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

fun = Tk()
textv = StringVar()

obj = LabelFrame(fun, text = "Text to Speech", font = 20, bd = 1)
obj.pack(fill = "both", expand = "yes", padx = 10, pady = 10)

lbl = Label(obj, text = "Text", font = 30)
lbl.pack(side = tk.LEFT, padx = 5)

text = Entry(obj, textvariable = textv, font = 30, width = 25, bd = 5)
text.pack(side = tk.LEFT, padx = 10)

btn = Button(obj, text = "Speak", font = 20, bg = "Black", fg = "White", command = speaknow)
btn.pack(side = tk.LEFT, padx = 10)

fun.title("Talha's Text to Speech Converter")
fun.geometry("400x200")
fun.resizable(False, False)
fun.mainloop()
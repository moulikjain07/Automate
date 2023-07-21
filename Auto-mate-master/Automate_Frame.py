from tkinter import *
from tkinter import PhotoImage

from Listen import listen


def initf_automate(f_automate):
    Grid.rowconfigure(f_automate, 0, weight=1)
    Grid.columnconfigure(f_automate, 1, weight=1)
    txt = Text(f_automate)
    txt.grid(row=0, column=1, sticky=N + S + E + W)

    Grid.rowconfigure(f_automate, 0, weight=1)
    Grid.columnconfigure(f_automate, 0, weight=1)
    panel = Frame(f_automate)
    panel.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.rowconfigure(panel, 0, weight=1)
    Grid.columnconfigure(panel, 0, weight=1)
    icon: PhotoImage = PhotoImage(file="microphone.png")
    listen_btn = Button(panel, text='Listen', command=lambda: listen(txt), image=icon, height=20, width=20)
    listen_btn.image = icon
    listen_btn.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.rowconfigure(panel, 1, weight=1)
    Grid.columnconfigure(panel, 0, weight=1)
    dummy = Frame(panel)
    dummy.grid(row=1, column=0, sticky=N + S + E + W)

from tkinter import *


def initf_menu(f_menu, f_automate, f_settings, f_about):
    for row_index in range(1):
        Grid.rowconfigure(f_menu, row_index, weight=1)
        for col_index in range(3):
            Grid.columnconfigure(f_menu, col_index, weight=1)

    btn1 = Button(f_menu, text='Automate', command=f_automate.lift)
    btn1.grid(row=0, column=0, sticky=N + S + E + W)

    btn2 = Button(f_menu, text='Settings', command=f_settings.lift)
    btn2.grid(row=0, column=1, sticky=N + S + E + W)

    btn3 = Button(f_menu, text='About', command=f_about.lift)
    btn3.grid(row=0, column=2, sticky=N + S + E + W)

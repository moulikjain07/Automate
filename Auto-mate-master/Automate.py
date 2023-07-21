from tkinter import *

from Menu_Frame import initf_menu
from About_Frame import initf_about
from Authenticate import authenticate
from Automate_Frame import initf_automate
from Settings_Frame import initf_settings


def initialize():
    root = Tk()
    root.title('Automate')
    root.state('zoomed')

    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    f = Frame(root)
    f.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.rowconfigure(f, 1, weight=8)
    Grid.columnconfigure(f, 0, weight=1)
    f_settings = Frame(f)
    f_settings.grid(row=1, column=0, sticky=N + S + E + W)
    f_about = Frame(f)
    f_about.grid(row=1, column=0, sticky=N + S + E + W)
    f_automate = Frame(f)
    f_automate.grid(row=1, column=0, sticky=N + S + E + W)

    initf_about(f_about)
    initf_settings(f_settings)
    initf_automate(f_automate)

    Grid.rowconfigure(f, 0, weight=1)
    Grid.columnconfigure(f, 0, weight=1)
    f_menu = Frame(f)
    f_menu.grid(row=0, column=0, sticky=N + S + E + W)

    initf_menu(f_menu, f_automate, f_settings, f_about)

    root.mainloop()


if __name__ == '__main__':
    if not authenticate():
        exit()
    initialize()

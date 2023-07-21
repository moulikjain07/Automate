from tkinter import *

keywords = [
    'google',
    'youtube',
    'email',
    'wikipedia',
    'news',
    'weather',
    'play MEDIA',
    'movie',
    'note',
    'day/date/time',
    'joke',
    'horoscope',
    '*general',
    'repeat',
    'bye'
]
actions = [
    'Search Google',
    'Play Youtube',
    'Send Email',
    'Search Wikipedia',
    'Read News headlines',
    'Get weather at current location',
    'Play local Media (audio/video)',
    'Play Movies',
    'Write/Read/Delete Notes',
    'Get current Day/Date/Time',
    'Read a Joke',
    'Read a Fortune',
    'General Conversations',
    'Repeat last sentence',
    'Exit application'
]


def initf_about(f_about):
    Grid.rowconfigure(f_about, 0, weight=1)
    Grid.columnconfigure(f_about, 0, weight=1)
    about = Frame(f_about)
    about.grid(row=0, column=0, sticky=N + E + W + S)

    Grid.rowconfigure(about, 0, weight=1)
    Grid.columnconfigure(about, 0, weight=1)
    summary = Label(
        about,
        font=('', 15),
        wraplength=800,
        justify=CENTER,
        text="'Automate' is your virtual personal assistant. It is developed to ease your internet access tasks while "
             "providing a human friendly experience. It can prove to be very helpful for digitally-illiterate users "
             "as well as the people overloaded with work."
    )
    summary.grid(row=0, column=0, sticky=N + E + W + S)

    Grid.rowconfigure(f_about, 1, weight=4)
    Grid.columnconfigure(f_about, 0, weight=1)
    details = Frame(f_about)
    details.grid(row=1, column=0, sticky=N + E + W + S)

    Grid.rowconfigure(details, 0, weight=1)
    Grid.columnconfigure(details, 0, weight=1)
    maps = Frame(details)
    maps.grid(row=0, column=0)

    hk = Label(maps, text='Keyword', borderwidth=2, relief="solid")
    hk.grid(row=0, column=0, sticky=N + E + W + S)
    ha = Label(maps, text='Action', borderwidth=2, relief="solid")
    ha.grid(row=0, column=1, sticky=N + E + W + S)

    i = 0
    for keyword, action in zip(keywords, actions):
        Label(maps, text=keyword, borderwidth=1, relief="solid").grid(row=i + 1, column=0, sticky=N + E + W + S)
        Label(maps, text=action, borderwidth=1, relief="solid").grid(row=i + 1, column=1, sticky=N + E + W + S)
        i += 1



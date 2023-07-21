import sqlite3
from tkinter import *
from tkinter import filedialog

from Database import update_users

themes = ''

voices = ''

music_path = ''
video_path = ''
movie_path = ''

email_id = ''

location = ''


def change_theme(*args):
    global themes
    theme = themes.get()
    if theme == 'Light Theme':
        update_users('theme', '0')
    elif theme == 'Dark Theme':
        update_users('theme', '1')


def change_voice(*args):
    global voices
    from Speak import tts
    gender = voices.get()
    if gender == 'Male':
        tts.Voice = tts.GetVoices().Item(0)
        update_users('voice', '0')
    elif gender == 'Female':
        tts.Voice = tts.GetVoices().Item(1)
        update_users('voice', '1')


def change_directory(i):
    global music_path, video_path, movie_path
    if i == 0:
        mp = filedialog.askdirectory(title='Select a music directory')
        if mp != '':
            music_path.set(mp)
            update_users('music', '"' + mp + '"')
    elif i == 1:
        vp = filedialog.askdirectory(title='Select a video directory')
        if vp != '':
            video_path.set(vp)
            update_users('video', '"' + vp + '"')
    elif i == 2:
        mop = filedialog.askdirectory(title='Select a movie directory')
        if mop != '':
            movie_path.set(mop)
            update_users('movie', '"' + mop + '"')


def update_email(email_entry, email_root):
    global email_id
    if email_entry != '':
        email_id.set(email_entry)
        update_users('email_id','"' + email_entry + '"')
        email_root.destroy()
    else:
        email_root.destroy()


def change_email_id(*args):
    email_root = Tk()
    email_root.title('Update Email ID')
    email_entry = Entry(email_root)
    email_entry.grid(row=0, column=0, sticky=N + E + W + S)
    Button(
        email_root,
        text='Update',
        command=lambda: update_email(email_entry.get(), email_root)
    ).grid(row=0, column=1, sticky=N + E + W + S)
    email_root.mainloop()


def update_location(location_entry, location_root):
    global location
    if location_entry != '':
        location.set(location_entry)
        update_users('location','"' + location_entry + '"')
        location_root.destroy()
    else:
        location_root.destroy()


def change_location(*args):
    location_root = Tk()
    location_root.title('Update Location')
    location_entry = Entry(location_root)
    location_entry.grid(row=0, column=0, sticky=N + E + W + S)
    Button(
        location_root,
        text='Update',
        command=lambda: update_location(location_entry.get(), location_root)
    ).grid(row=0, column=1, sticky=N + E + W + S)
    location_root.mainloop()


def initf_settings(f_settings):
    global themes, voices, music_path, video_path, movie_path, email_id, location

    Grid.rowconfigure(f_settings, 0, weight=1)
    Grid.columnconfigure(f_settings, 0, weight=1)
    control_panel = Frame(f_settings)
    control_panel.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.columnconfigure(control_panel, 0, weight=1)

    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    cur_user_data = cursor.execute('SELECT * FROM current_user').fetchone()
    con.close()

    options1 = [
        'Light Theme',
        'Dark Theme'
    ]
    themes = StringVar()
    themes.set(options1[cur_user_data[2]])
    themes.trace('w', change_theme)
    f1 = Frame(control_panel, bd=1, relief=RAISED)
    f1.grid(row=0, column=0, sticky=E + W)
    Grid.columnconfigure(f1, 0, weight=1)
    Label(f1, text='Set Theme').grid(row=0, column=0, sticky=W)
    OptionMenu(f1, themes, *options1).grid(row=0, column=1, sticky=E)

    options2 = [
        'Male',
        'Female'
    ]
    voices = StringVar()
    voices.set(options2[cur_user_data[3]])
    voices.trace('w', change_voice)
    f2 = Frame(control_panel, bd=1, relief=RAISED)
    f2.grid(row=1, column=0, sticky=E + W)
    Grid.columnconfigure(f2, 0, weight=1)
    Label(f2, text="Set Assistant's voice").grid(row=0, column=0, sticky=W)
    OptionMenu(f2, voices, *options2).grid(row=0, column=1, sticky=E)

    music_path = StringVar()
    music_path.set(cur_user_data[4])
    f3 = Frame(control_panel, bd=1, relief=RAISED)
    f3.grid(row=2, column=0, sticky=E + W)
    Grid.columnconfigure(f3, 0, weight=1)
    Grid.columnconfigure(f3, 1, weight=1)
    Label(f3, text="Set Music Directory").grid(row=0, column=0, sticky=W)
    Label(f3, textvariable=music_path).grid(row=0, column=1, sticky=E + W)
    Button(f3, text='Change directory', command=lambda: change_directory(0)).grid(row=0, column=2, sticky=E)

    video_path = StringVar()
    video_path.set(cur_user_data[5])
    f4 = Frame(control_panel, bd=1, relief=RAISED)
    f4.grid(row=3, column=0, sticky=E + W)
    Grid.columnconfigure(f4, 0, weight=1)
    Grid.columnconfigure(f4, 1, weight=1)
    Label(f4, text="Set Video Directory").grid(row=0, column=0, sticky=W)
    Label(f4, textvariable=video_path).grid(row=0, column=1, sticky=E + W)
    Button(f4, text='Change directory', command=lambda: change_directory(1)).grid(row=0, column=2, sticky=E)

    movie_path = StringVar()
    movie_path.set(cur_user_data[6])
    f5 = Frame(control_panel, bd=1, relief=RAISED)
    f5.grid(row=4, column=0, sticky=E + W)
    Grid.columnconfigure(f5, 0, weight=1)
    Grid.columnconfigure(f5, 1, weight=1)
    Label(f5, text="Set Movie Directory").grid(row=0, column=0, sticky=W)
    Label(f5, textvariable=movie_path).grid(row=0, column=1, sticky=E + W)
    Button(f5, text='Change directory', command=lambda: change_directory(2)).grid(row=0, column=2, sticky=E)

    email_id = StringVar()
    email_id.set(cur_user_data[7])
    f6 = Frame(control_panel, bd=1, relief=RAISED)
    f6.grid(row=5, column=0, sticky=E + W)
    Grid.columnconfigure(f6, 0, weight=1)
    Grid.columnconfigure(f6, 1, weight=1)
    Label(f6, text="Set Email ID").grid(row=0, column=0, sticky=W)
    Label(f6, textvariable=email_id).grid(row=0, column=1, sticky=E + W)
    Button(f6, text='Change Email ID', command=lambda: change_email_id()).grid(row=0, column=2, sticky=E)

    location = StringVar()
    location.set(cur_user_data[8])
    f7 = Frame(control_panel, bd=1, relief=RAISED)
    f7.grid(row=6, column=0, sticky=E + W)
    Grid.columnconfigure(f7, 0, weight=1)
    Grid.columnconfigure(f7, 1, weight=1)
    Label(f7, text="Set Location").grid(row=0, column=0, sticky=W)
    Label(f7, textvariable=location).grid(row=0, column=1, sticky=E + W)
    Button(f7, text='Change Location', command=lambda: change_location()).grid(row=0, column=2, sticky=E)

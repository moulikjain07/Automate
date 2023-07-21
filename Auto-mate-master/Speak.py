import sqlite3
from tkinter import *
from win32com.client import Dispatch

con = sqlite3.connect('automate.db')
cursor = con.cursor()
cur_user_voice = cursor.execute('SELECT * FROM current_user').fetchone()[3]
tts = Dispatch("SAPI.SpVoice")
tts.Voice = tts.GetVoices().Item(cur_user_voice)
con.close()

repeat_text = ''


def speak(query, txt):
    global tts, repeat_text
    repeat_text = query
    txt.insert(INSERT, 'Automate : ')
    txt.insert(INSERT, query)
    txt.insert(INSERT, '\n')
    txt.update()
    tts.Speak(query)

import speech_recognition
from tkinter import *

from Speak import speak


def take_command(txt):
    while True:
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print('Listening....')
            txt.insert(INSERT, 'Listening....\n')
            txt.update()
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print('Recognizing...')
            txt.insert(INSERT, 'Recognizing...\n')
            txt.update()
            query = r.recognize_google(audio, language='en-in')
            print('User : ' + query + '\n')
            txt.insert(INSERT, 'User : ' + query + '\n')
            txt.update()
        except Exception as e:
            print(e)
            speak("Say again please...", txt)
            continue
        return query

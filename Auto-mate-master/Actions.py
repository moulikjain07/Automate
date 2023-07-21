import os
import sqlite3
import urllib
import webbrowser
from datetime import datetime
from tkinter import *
from urllib.request import urlopen

import psutil
import pyowm
import wikipedia as wiki
from bs4 import BeautifulSoup
from horoscope_generator import HoroscopeGenerator

import GeneralConversations
from Database import get_note, set_note, clear_notes
from EmailLogin import EmailLogin
from Input import take_command
from Speak import speak

media_name = ''
media_flag = False

movie_list = dict()
movie_count = 1

joke_count = 0


def general_conversation(query, txt):
    dictionary = dict([('who_are_you', ['what', 'name', 'who', 'are', 'you', 'identification']),
                       ('toss_coin', ['heads', 'tails', 'flip', 'toss', 'coin']),
                       ('how_am_i', ['how', 'am', 'i', 'look', 'looking']),
                       ('who_am_i', ['who', 'am', 'i']),
                       ('where_born', ['who', 'made', 'created', 'where', 'born', 'birth']),
                       ('how_are_you', ['how', 'are', 'you']),
                       ('are_you_up', ['you', 'up']),
                       ('love_you', ['love', 'you']),
                       ('marry_me', ['marry', 'me'])])

    score = dict([('who_are_you', 0),
                  ('toss_coin', 0),
                  ('how_am_i', 0),
                  ('who_am_i', 0),
                  ('where_born', 0),
                  ('how_are_you', 0),
                  ('are_you_up', 0),
                  ('love_you', 0),
                  ('marry_me', 0)])

    words = query.split(' ')

    for word in words:
        for keyword in dictionary:
            for value in dictionary.get(keyword):
                if word == value:
                    score[keyword] += 1
                    break

    max_score = max(score, key=score.get)

    if score.get(max_score) == 0:
        speak('I am not sure about this', txt)
    else:
        getattr(GeneralConversations, max_score)(query, txt)


def search_song(root, txt):
    global media_name, media_flag
    if media_flag:
        return
    for file in os.listdir(root): 
        cur_path = os.path.join(root, file)
        if os.path.isdir(cur_path):
            search_song(cur_path, txt)
        else:
            if file.endswith('.mp3'):
                if re.search(media_name, file.lower()):
                    media_flag = True
                    speak('Playing song ' + media_name, txt)
                    os.startfile(cur_path)
                    break


def search_video(root, txt):
    global media_name, media_flag
    if media_flag:
        return
    for file in os.listdir(root):
        cur_path = os.path.join(root, file)
        if os.path.isdir(cur_path):
            search_video(cur_path, txt)
        else:
            if file.endswith('.mp4') or file.endswith('.MP4') or file.endswith('.mkv') or file.endswith(
                    '.MKV') or file.endswith('.avi') or file.endswith('.WEBM'):
                if re.search(media_name, file.lower()):
                    media_flag = True
                    speak('Playing video ' + media_name, txt)
                    os.startfile(cur_path)
                    break


def play_media(query, txt):
    from Settings_Frame import music_path, video_path
    global media_name, media_flag
    media_flag = False
    media_name = query.replace('play', '').replace('mp3', '').replace('song', '').replace('video', '').lower().strip()
    if 'mp3' in query or 'song' in query:
        search_song(music_path.get(), txt)
    else:
        search_video(video_path.get(), txt)
    if not media_flag:
        speak('Sorry, the media is not available.', txt)


def search_movie(root, txt):
    global movie_list, movie_count
    for file in os.listdir(root):
        cur_path = os.path.join(root, file)
        if os.path.isdir(cur_path):
            search_movie(cur_path, txt)
        elif file.endswith('.mp4') or file.endswith('.MP4') or file.endswith('.mkv') or file.endswith(
                '.MKV') or file.endswith('.avi') or file.endswith('webm') or file.endswith('.WEBM'):
            txt.insert(INSERT, str(movie_count) + ' ' + file + '\n')
            txt.update()
            movie_list[movie_count] = cur_path
            movie_count += 1


def movie(query, txt):
    from Settings_Frame import movie_path
    global movie_count
    movie_count = 0
    search_movie(movie_path.get(), txt)
    if movie_count == 0:
        speak('The movies folder is empty.', txt)
        return
    while True:
        try:
            speak('Select a number', txt)
            os.startfile(movie_list[int(take_command(txt))])
            break
        except KeyError:
            speak('Invalid number. Please select a number in the given range.', txt)
            continue


def google(query, txt):
    speak("Searching Google", txt)
    query = query.replace('search', '').replace('google', '').replace('for', '').strip().replace(" ", "+")
    webbrowser.open('https://www.google.com/search?q=' + query)


def youtube(query, txt):
    speak('Opening Youtube', txt)
    query = query.replace('youtube', '').replace('play', '').replace('video', '').strip().replace(" ", "+")
    htm_content = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + query)
    results = re.findall('href=\"/watch\\?v=(.{11})', htm_content.read().decode())
    webbrowser.open("https://www.youtube.com/watch?v=" + results[0])


def wikipedia(query, txt):
    try:
        speak('searching wikipedia', txt)
        query = query.replace('search', '').replace('wikipedia', '').replace('for', '').strip()
        results = wiki.summary(query, sentences=2)
        speak('according to wikipedia', txt)
        speak(results, txt)
    except Exception as e:
        speak(e, txt)


def news(query, txt):
    news_url = "https://news.google.com/news/rss"
    client = urlopen(news_url)
    xml_page = client.read()
    client.close()
    soup_page = BeautifulSoup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    del news_list[3:]
    for news_item in news_list:
        speak(news_item.title.text, txt)


def weather(query, txt):
    owm = pyowm.OWM('61cf9c73e72fb837f80c3e97ecd03a37')
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    location = cursor.execute('SELECT * FROM current_user').fetchone()[8]
    con.close()
    report = owm.weather_at_place(location)
    result = report.get_weather()
    detailed_status = result.get_detailed_status()
    temp = result.get_temperature(unit='celsius')
    weather_result = 'It is ' \
                     + detailed_status + ' in ' \
                     + location + '. The temperature is ' \
                     + str(temp.get('temp')) + '° Celsius.'
    speak(weather_result, txt)


def day_date_time(query, txt):
    if 'time' in query:
        speak("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'), txt)
    if 'date' in query:
        speak("The date is " + datetime.strftime(datetime.now(), '%m/%d/%Y'), txt)
    if 'day' in query:
        speak("The day is " + datetime.strftime(datetime.now(), '%A'), txt)


def horoscope(query, txt):
    speak((HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence())), txt)


def joke(query, txt):
    global joke_count
    jokes = [
        'What happens to a frogs car when it breaks down? It gets toad away.',
        'Why was six scared of seven? Because seven ate nine.',
        'Why are mountains so funny? Because they are hill areas.',
        'Have you ever tried to eat a clock?'
        'I hear it is very time consuming.',
        'What happened when the wheel was invented? A revolution.',
        'What do you call a fake noodle? An impasta!',
        'Did you hear about that new broom? It is sweeping the nation!',
        'What is heavy forward but not backward? Ton.',
        'No, I always forget the punch line.'
    ]
    speak(jokes[joke_count], txt)
    joke_count += 1


def note(query, txt):
    if 'read' in query or 'show' in query or 'tell' in query or 'display' in query or 'what' in query:
        get_note(txt)
    elif 'clear' in query or 'delete' in query or 'erase' in query:
        clear_notes(txt)
    else:
        query = query.replace('note', '').replace('memorize', '').strip()
        if query == '':
            speak('There is nothing to note.', txt)
            return
        set_note(query, txt)


def email(query, txt):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    email_id = cursor.execute('SELECT * FROM current_user').fetchone()[7]
    con.close()
    EmailLogin(email_id, Toplevel(), txt)


def repeat(query, txt):
    from Speak import repeat_text
    speak(repeat_text, txt)


def bye(query, txt):
    speak('Goodbye', txt)
    for process in psutil.process_iter():
        proc_name = process.name()
        if proc_name == 'chrome.exe':
            process.kill()
    exit()

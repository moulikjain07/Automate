import random
import sqlite3

from Speak import speak


def who_are_you(query, txt):
    messages = [
        "I am Automate your loyal personal assistant.",
        "Automate, didn't I tell you before?",
        "You ask that so many times! I am automate."
    ]
    speak(random.choice(messages), txt)


def toss_coin(query, txt):
    outcomes = ['heads', 'tails']
    speak('I just flipped a coin. It shows ' + random.choice(outcomes), txt)


def how_am_i(query, txt):
    replies = [
        'You are goddamn handsome!',
        'My knees go weak when I see you.',
        'You look like the kindest person that I have met.'
    ]
    speak(random.choice(replies), txt)


def who_am_i(query, txt):
    con=sqlite3.connect('automate.db')
    cursor=con.cursor()
    name = cursor.execute('SELECT * FROM current_user').fetchone()[0]
    speak('You are ' + name + ', a brilliant person.', txt)
    con.close()


def where_born(query, txt):
    speak('I was created by code.', txt)


def how_are_you(query, txt):
    speak('I am fine, thank you.', txt)


def are_you_up(query, txt):
    speak('For you, always.', txt)


def love_you(query, txt):
    replies = [
        'I love you too.',
        'You are looking for love in the wrong place.'
    ]
    speak(random.choice(replies), txt)


def marry_me(query, txt):
    speak('I have been receiving a lot of marriage proposals recently.', txt)
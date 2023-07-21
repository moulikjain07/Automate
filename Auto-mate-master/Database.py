from datetime import datetime
import sqlite3
from Speak import speak


def set_note(query, txt):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    username = cursor.execute('SELECT * FROM current_user').fetchone()[0]
    cursor.execute(
        "INSERT INTO notes VALUES (?, ?, ?)",
        (username, query, datetime.strftime(datetime.now(), '%d-%m-%Y'))
    )
    con.commit()
    con.close()
    speak('Your note has been saved.', txt)


def get_note(txt):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    username = cursor.execute('SELECT * FROM current_user').fetchone()[0]
    rows = cursor.execute('SELECT * FROM notes WHERE username = "' + username + '"').fetchall()
    if len(rows) == 0:
        speak('You have no notes', txt)
    else:
        speak('Your notes are as follows :', txt)
        for row in rows:
            speak(row[1], txt)
    con.close()


def clear_notes(txt):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    username = cursor.execute('SELECT * FROM current_user').fetchone()[0]
    cursor.execute('DELETE FROM notes WHERE username = "' + username + '"')
    con.commit()
    con.close()
    speak('All notes have been erased.', txt)


def update_users(setting, value):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    cursor.execute('UPDATE current_user SET ' + setting + '=' + value)
    username = cursor.execute('SELECT * FROM current_user').fetchone()[0]
    cursor.execute('DELETE FROM users WHERE username = "' + username + '"')
    cursor.execute('INSERT INTO users SELECT * FROM current_user')
    con.commit()
    con.close()

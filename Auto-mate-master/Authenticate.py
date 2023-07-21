from tkinter import *
import sqlite3

flag = False
login_root = Tk()


def check_credentials(username_entry, password_entry):
    global flag
    flag = False
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    rows = cursor.execute('SELECT username,password FROM users WHERE username="' + username_entry + '"').fetchall()
    if len(rows) == 0:
        print('No such account')
    elif len(rows) == 1:
        if rows[0][1] == password_entry:
            flag = True
            login_root.destroy()
            cursor.execute('DELETE FROM current_user')
            cursor.execute('INSERT INTO current_user SELECT * FROM users WHERE username = "' + username_entry + '"')
            con.commit()
        else:
            print('Incorrect password')
    else:
        print('Database error: More than one users with same username found!')
    con.close()


def new_entry(username_entry, password_entry):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    rows = cursor.execute('SELECT username,password FROM users WHERE username="' + username_entry + '"').fetchall()
    if len(rows) == 0:
        cursor.execute(
            'INSERT INTO users (username,password) VALUES ("' + username_entry + '", "' + password_entry + '")'
        )
        con.commit()
        print('Account created')
    elif len(rows) == 1:
        print('User already exists')
    else:
        print('Database error: More than one users with same username found!')
    con.close()


def del_entry(username_entry, password_entry):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    rows = cursor.execute('SELECT username,password FROM users WHERE username="' + username_entry + '"').fetchall()
    if len(rows) == 0:
        print('No such account')
    elif len(rows) == 1:
        if rows[0][1] == password_entry:
            cursor.execute('DELETE FROM users WHERE username="' + username_entry + '"')
            con.commit()
            print('Account deleted')
        else:
            print('Incorrect password')
    else:
        print('Database error: More than one users with same username found!')
    con.close()


def login_initialize():
    login_root.title('Login')

    login_frame = Frame(login_root, padx=10, pady=10)
    login_frame.grid(row=0, column=0, sticky=N + E + W + S)

    Label(login_frame, text='LOGIN', font=('', 35), pady=10).grid(row=0, column=0, sticky=N + S + E + W)
    Label(login_frame, text='Username : ', font=('', 20), pady=5, padx=5).grid(row=1, column=0, sticky=N + S + E + W)
    Label(login_frame, text='Password : ', font=('', 20), pady=5, padx=5).grid(row=2, column=0, sticky=N + S + E + W)

    username_entry = Entry(login_frame, bd=5, font=('', 15))
    username_entry.grid(row=1, column=1, sticky=N + S + E + W)
    password_entry = Entry(login_frame, show='*', bd=5, font=('', 15))
    password_entry.grid(row=2, column=1, sticky=N + S + E + W)

    Button(
        login_frame,
        text='Del User',
        bd=3, font=('', 15), padx=5, pady=5,
        command=lambda: del_entry(username_entry.get(), password_entry.get())
    ).grid(row=3, column=0, sticky=N + S + E + W)
    Button(
        login_frame,
        text='Sign Up',
        bd=3, font=('', 15), padx=5, pady=5,
        command=lambda: new_entry(username_entry.get(), password_entry.get())
    ).grid(row=3, column=1, sticky=N + S + E + W)
    Button(
        login_frame,
        text='Login',
        bd=3, font=('', 15), padx=5, pady=5,
        command=lambda: check_credentials(username_entry.get(), password_entry.get())
    ).grid(row=4, column=0, columnspan=2, sticky=N + S + E + W)

    login_root.mainloop()


def authenticate():
    global flag
    login_initialize()
    if flag:
        return True
    else:
        return False

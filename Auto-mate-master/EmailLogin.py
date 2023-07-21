from _socket import gaierror
from smtplib import SMTP, SMTPConnectError, SMTPAuthenticationError, SMTPServerDisconnected
from tkinter import *
from tkinter import messagebox

from EmailSend import EmailSend
from Speak import speak


class EmailLogin:

    def __init__(self, email_id, master, txt):

        try:
            self.server = SMTP('smtp.gmail.com', 587)
        except (gaierror, SMTPConnectError, SMTPServerDisconnected):
            speak('The server could not be reached', txt)

        self.email_id = email_id

        self.master = master
        self.master.title('Login to Gmail')

        self.txt = txt

        email_auth_frame = Frame(self.master, padx=10, pady=10)
        email_auth_frame.grid(row=0, column=0, sticky=N + S + E + W)

        Label(
            email_auth_frame,
            text='Enter Gmail Password',
            font=('', 25),
            pady=10
        ).grid(row=0, column=0, sticky=N + E + W + S, columnspan=2)
        Label(
            email_auth_frame,
            text='Password : ',
            font=('', 20),
            pady=5,
            padx=5
        ).grid(row=2, column=0, sticky=N + E + W + S)

        password_entry = Entry(email_auth_frame, show='*', bd=5, font=('', 15))
        password_entry.grid(row=2, column=1, sticky=N + S + E + W)

        Button(
            email_auth_frame,
            text='Sign in',
            bd=3,
            font=('', 15),
            padx=5,
            pady=5,
            command=lambda: self.gmail_sign_in(password_entry.get())
        ).grid(row=3, column=1, sticky=N + S + E + W)

    def gmail_sign_in(self, password):
        self.master.destroy()
        try:
            self.server.starttls()
            self.server.login(self.email_id, password)
        except (gaierror, SMTPConnectError, SMTPServerDisconnected):
            speak('The server could not be reached', self.txt)
        except SMTPAuthenticationError:
            speak('Invalid credentials', self.txt)
        else:
            EmailSend(self.email_id, self.server, Toplevel(), self.txt)

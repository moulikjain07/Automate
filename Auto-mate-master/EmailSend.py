from smtplib import SMTPRecipientsRefused, SMTPServerDisconnected
from tkinter import *
from tkinter import messagebox

from Speak import speak


class EmailSend:
    def __init__(self, email_id, server, master, txt):

        self.email_id = email_id
        self.server = server
        self.txt = txt

        self.master = master
        self.master.title('Send Email')

        Label(
            self.master,
            text='Recipient(s) : ',
            font=('', 15),
            pady=5,
            padx=5
        ).grid(row=0, column=0, sticky=N + E + W + S)
        self.recipients = Entry(self.master, bd=5, font=('', 15))
        self.recipients.grid(row=0, column=1, sticky=N + E + W + S, columnspan=3)
        Button(
            self.master,
            text='Send',
            command=lambda: self.send_email(self.recipients.get().replace(' ', '').split(','),
                                            self.subject.get().strip(),
                                            self.message.get('1.0', 'end-1c'))
        ).grid(row=0, column=4, sticky=N + E + W + S)

        Label(
            self.master,
            text='Subject : ',
            font=('', 15),
            pady=5,
            padx=5
        ).grid(row=1, column=0, sticky=N + E + W + S)
        self.subject = Entry(self.master, bd=5, font=('', 15))
        self.subject.grid(row=1, column=1, sticky=N + E + W + S, columnspan=4)

        self.message = Text(self.master)
        self.message.grid(row=2, column=0, rowspan=5, columnspan=5)

    def send_email(self, recipient, subject, body):
        sender = self.email_id
        receiver = recipient if isinstance(recipient, list) else [recipient]
        if len(receiver) == 0 or body == '':
            speak('Please type the message content',self.txt)
            return
        self.master.destroy()
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (sender, ", ".join(receiver), subject, body)
        try:
            self.server.sendmail(sender, receiver, message)
            self.server.close()
        except SMTPRecipientsRefused:
            speak('Recipient Email ID incorrect', self.txt)
        except SMTPServerDisconnected:
            speak('The server could not be reached', self.txt)
        else:
            speak('The mail was delivered successfully.', self.txt)

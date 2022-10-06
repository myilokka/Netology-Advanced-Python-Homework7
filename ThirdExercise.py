import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser
import os


class MailBox:

    def __init__(self):
        if not os.path.exists(path):
            print("Создайте конфигурационый файл!")
        else:
            config = configparser.ConfigParser()
            config.read(path)
            self.GMAIL_SMTP = config.get("Settings", "GMAIL_SMTP")
            self.GMAIL_IMAP =  config.get("Settings", "GMAIL_IMAP ")
            self.login = config.get("Settings", "login")
            self.password =  config.get("Settings", "password")
            self.subject =  config.get("Settings", "subject")
            self.recipients = config.get("Settings", "recipients")
            self.message = config.get("Settings", "message")
            self.header = config.get("Settings", "header")

    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        ms_server = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms_server.ehlo()
        ms_server.starttls()
        ms_server.ehlo()
        ms_server.login(self.login, self.password)
        ms_server.sendmail(self.login, self.recipients, msg.as_string())
        ms_server.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


def create_config(path):

    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "GMAIL_SMTP", "smtp.gmail.com")
    config.set("Settings", "GMAIL_IMAP ", "imap.gmail.com")
    config.set("Settings", "login", "login@gmail.com")
    config.set("Settings", "password", "password")
    config.set("Settings", "subject", "Subject")
    config.set("Settings", "recipients", "['vasya@email.com', 'petya@email.com']")
    config.set("Settings", "message", "Message")
    config.set("Settings", "header", "None")

    with open(path, "w") as config_file:
        config.write(config_file)




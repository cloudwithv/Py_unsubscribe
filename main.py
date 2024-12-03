from dotenv import load_dotenv
import imaplib
import email
import os
load_dotevn()

username = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

def connect_to_email():
    mail = imaplib.IMAP4_SSL('smtp-mail.outlook.com')
    mail.login(username, password)
    mail.select('inbox')
    return mail

    def search_for_email():
        mail = connect_to_email()
        _, search_data = mail.search(None, '(BODY "unsubscribe")')

        mail.logout()
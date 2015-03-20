from flask.ext.mail import Message
from charity_bets import mail
from flask import render_template, current_app
from threading import Thread


def send_async_email(app, message):
    with app.app_context():
        mail.send(message)

def send_email(subject, sender, recipients, text_body, html_body):
    app = current_app._get_current_object()
    message = Message(subject, sender=sender, recipients=recipients)
    message.body = text_body
    message.html = html_body
    thr = Thread(target=send_async_email, args=[app, message])
    thr.start()
    return thr

def bet_creation_notification(key):
    send_email("New charity signed up, new key",
               "betsforcharity@gmail.com",
               "betsforcharity@gmail.com",
               key)

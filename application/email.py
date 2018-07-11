from flask_mail import Message
from application import mail
from flask import render_template
from application import application


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_contact_info_email(date, name, phone_number, description):
    send_email('Spark Construction New Contact Request',
               sender='mdstest10010011@gmail.com',
               recipients=['msalvatierra1356@gmail.com'],
               text_body=render_template('email/contact_info_email.txt',
                                         date=date,
                                         name=name,
                                         phone_number=phone_number,
                                         description=description),
               html_body=render_template('email/contact_info_email.html',
                                         date=date,
                                         name=name,
                                         phone_number=phone_number,
                                         description=description))




from __future__ import absolute_import, unicode_literals
from celery import shared_task
import smtplib
import string 
from random import choice
from email.message import EmailMessage

def send_email(reciever_email):
    msg = EmailMessage()
    otp =  ''.join(choice(string.digits) for _ in range(4))
    msg.set_content(str(otp))
    msg['Subject'] = 'OTP Verification'
    msg['From'] = "buttonchimken@gmail.com"
    msg['To'] = str(reciever_email)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("buttonchimken@gmail.com","fydqvuoljaadwpkw")
    server.send_message(msg)
    server.quit()
    return otp

@shared_task()
def mail_otp(reciever_email):
    try:
        otp = send_email(reciever_email)
        return otp
    except:
        return ""
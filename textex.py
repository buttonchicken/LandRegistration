import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('This is my message')

msg['Subject'] = 'Subject'
msg['From'] = "buttonchimken@gmail.com"
msg['To'] = "aditya.mutharia@gmail.com"

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("buttonchimken@gmail.com","fydqvuoljaadwpkw")
server.send_message(msg)
server.quit()
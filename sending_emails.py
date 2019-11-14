from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests

message = MIMEMultipart()
message['from'] = 'Mosh Hamedani'
message['to'] = 'cientista77@gmail.com'
message['subject'] = 'This is a test!'
message.attach('Body')

with smtplib.SMTP(host='smtp.gmail.com', port=535) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('cientista77@gmail.com', 'today is Carlos experience with python email')
    smtp.send_message(message)
    print('sent...')

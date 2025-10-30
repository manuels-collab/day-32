import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

#EMAIL CONFIG
sender_email = 'mycompanyprince@gmail.com'
receiver_email = 'manuelsdesk0029@gmail.com'
password = 'oyfxsxzcudajllxf'

#Create the email content
subject = 'Test Mail'
body = "Hello, this is a another birthday wish from python!"

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

message.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)

print('EMAIL SENT SUCCESSFULLY')
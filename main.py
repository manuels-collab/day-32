 ##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
from random import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 1. Update the birthdays.csv
#Reading the data

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv('birthdays.csv')
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
current_date = f'{year} {month} {day}'
data_dict = data.to_dict(orient='records')
for item in data_dict:
    if month == item['month'] and day == item['day']:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        birthday_letters = choice(['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt'])

        with open(birthday_letters, 'r') as file:
            file_content = f'{file.read()}'

        new_file = file_content.replace('[NAME]', item['name'])
# 4. Send the letter generated in step 3 to that person's email address.
    #LETTER BODY
        sender_email = 'mycompanyprince@gmail.com'
        receiver_email = 'manuelsdesk0029@gmail.com'
        password = 'oyfxsxzcudajllxf'
    #LETTER CONTENT
        subject = 'HAPPY BIRTHDAY'
        body = new_file


        messages = MIMEMultipart()
        messages['From'] = sender_email
        messages['To'] = receiver_email
        messages['Subject'] = subject

        messages.attach(MIMEText(body, "plain"))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(messages)
print("Messages sent sucessfully")




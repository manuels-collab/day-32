import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

api_key = "be2b744511fb2d76bec521e2531e2578"
latitude = 5.181740
longitude = 7.715100

#Making a request
parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/"
             "2.5/forecast", params=parameters)

will_rain = False
response.raise_for_status()
weather_data = response.json()
for item in weather_data['list']:
    if int(item['weather'][0]['id']) < 700:
        will_rain = True
if will_rain:
    print("Bring an Umbrella")
    #User info
    user_name = 'my email'
    user_password = 'my password'
    #Create Message Body
    subject = f'Raining Alert'
    body = "Hey it'll rain today before 6pm"

    message = MIMEMultipart()
    message['To'] = user_name
    message['From'] = user_name
    message['Subject'] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user_name, user_password)
        server.send_message(message)
    print("Email sent successfully")

import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import time

MY_LAT =  5.172110# Your latitude
MY_LONG = 7.999480 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()

iss_latitude = 7.172110 #float(data["iss_position"]["latitude"])
iss_longitude = 3.4444#float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def set_current_position(lat, long):
    global iss_latitude, iss_longitude
    if lat-5 <= iss_latitude <= lat + 5 or long-5 <= iss_longitude <= long+5:
            print(iss_latitude)
            print(iss_longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = 17#int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = 7#int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()


#If the ISS is close to my current position
# and it is currently dark
if time_now.hour >= sunset or time_now.hour <= sunrise:
    set_current_position(MY_LAT, MY_LONG)
# Then email me to tell me to look up.
    #Create an email
    while True:
        my_email = "My email"
        password = "My Password"
        subject = "ISS in the sky"
        body = "Look up in the sky, the ISS IS PASSING"

        message = MIMEMultipart()
        message['From'] = my_email
        message['To'] = my_email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(my_email, password)
            server.send_message(message)
        print("Messages sent successfully")
# BONUS: run the code every 60 seconds.




import requests
from datetime import datetime
import smtplib
import time

#Essential variables
MY_LAT = float(MY_LAT) # Your latitude
MY_LONG = float(MY_LONG) # Your longitude
MY_POSITION = (MY_LAT,MY_LONG)

my_email = "MY_EMAIL"
password = "MY_PASSWORD"

#API request to check International Space Station (ISS) longitude and latitude
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

#print(data)
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#print(iss_latitude)
#print(iss_longitude)

#Checking if your position is within +5 or -5 degrees of the ISS position.
def check_position():
    if ((MY_LAT-5) <= iss_latitude <= (MY_LAT+5)) and ((MY_LONG-5) <= iss_longitude <= (MY_LONG+5)):
        return True
    else:
        return False

#API parameters needed to get the sunrise and sunset times for your location
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()
data2 = response.json()

sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour= time_now.hour
#print(current_hour)

#Checking if the current time is actually at night
def check_daytime():
    if (current_hour > sunrise) and (current_hour < sunset):
        return False
    else:
        return True


final_position = check_position()
#print(final_position)
final_time = check_daytime()
#print(final_time)

#Checking if the ISS position is around your position and if your current time is actually at night.
# If these two requirements are true, then you will get notification email. This will run every 5 min
while True:
    time.sleep(300)
    if (final_position == True) and (final_time== True):
        with smtplib.SMTP("SMTP_ADDRESS_HERE") as connection:
            connection.starttls()
            connection(login=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="DESTINATION_EMAIL",
                msg="Subject: ISS information\n\nLook up! Satellite is flying above you")
    else:
        pass



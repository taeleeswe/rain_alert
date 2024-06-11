import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWN_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("OWN_AUTH_TOKEN")

weather_params = {
    "lat": 40.713024,
    "lon": -74.035017,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["Hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an ☂️",
        from_="+18449224051",
        to="+13473661803"
    )
    print(message.status)
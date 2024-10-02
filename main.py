import requests
from twilio.rest import Client

API_KEY = "Your Api key"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"  # weather api endpoint
account_sid = "Your Account Sid"
auth_token = "Your Authh Token"

weather_params = {  # parameters for the data
    "lat": 59.913868,
    "lon": 10.752245,
    "appid": API_KEY
}

response = requests.get(OWN_ENDPOINT, params=weather_params)

weather_data = response.json()["weather"][0]

rain_data = weather_data["id"]
print(rain_data)

client = Client(account_sid, auth_token)

if rain_data < 700:
    message = client.messages\
        .create(
        from_='Your twilio number',
        body='Ahoy! This message was sent from my Twilio phone number! Just to remind you it may rain today, its better to keep'
             'umbrella !',
        to='recepient number'
    )
    print(message.status)

import requests
from twilio.rest import Client

API_KEY = "be3af95af67beaa77f5732e06d3789a0"
LONG = -9.056790
LAT = 53.270668
AUTH_SID = "AC4a75114d1ef39bb2186406ed6a1668f8"
AUTH_TOKEN = "215e3c0a56003e9d6b09a46da62d55ca"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()["list"]
is_raining = False
for item in data:
    id = item["weather"][0]["id"]
    if id < 800:
        is_raining = True

if is_raining:
    client = Client(AUTH_SID,AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today, Remember to bring an umberlla",
        from_="+14156504439",
        to="+353874796931"
    )
    print(message.status)


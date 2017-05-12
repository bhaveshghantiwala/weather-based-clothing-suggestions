import requests
import json
from apiKey import getOpenWeatherMapAPI

def getWeatherData():
    #get geolocation
    geoloc = requests.get("http://freegeoip.net/json").json()

    #store latitude and longitude
    lat = geoloc['latitude']
    lon = geoloc['longitude']

    #get local weather based on latitude and longitude
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather?lat="
            + str(lat) + "&lon="+ str(lon) 
            + "&appid="
            + getOpenWeatherMapAPI()).json()

    return weather

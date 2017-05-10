import requests
import json
import pprint

#get geolocation
geoloc = requests.get("http://freegeoip.net/json").json()

#store latitude and longitude
lat = geoloc['latitude']
lon = geoloc['longitude']

#get local weather based on latitude and longitude
weather = requests.get("http://api.openweathermap.org/data/2.5/weather?lat="
        + str(lat) + "&lon="+ str(lon) 
        + "&appid=66a8e5b59568e93c8e6093c555a48950").json()

pprint.pprint(weather)

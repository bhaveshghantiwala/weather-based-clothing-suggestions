from weatherDataCalc import *
import pprint
import requests

weatherData = requests.get("http://api.openweathermap.org/data/2.5/weather?"
        + "q=London"
        + "&appid=66a8e5b59568e93c8e6093c555a48950").json()

currTemp = weatherData['main']['temp']

currTemp = kelvinToFar(currTemp)

currWindSpeed = weatherData['wind']['speed']
currWeatherCond = ()
for i in weatherData['weather']:
    currWeatherCond += (i['id'],)

pprint.pprint(weatherData)
print normalizedWeatherData(currTemp, currWeatherCond)


weatherData = requests.get("http://api.openweathermap.org/data/2.5/weather?"
        + "q=Copenhagen"
        + "&appid=66a8e5b59568e93c8e6093c555a48950").json()

currTemp = weatherData['main']['temp']

currTemp = kelvinToFar(currTemp)

currWindSpeed = weatherData['wind']['speed']
currWeatherCond = ()
for i in weatherData['weather']:
    currWeatherCond += (i['id'],)


pprint.pprint(weatherData)
print normalizedWeatherData(currTemp, currWeatherCond)

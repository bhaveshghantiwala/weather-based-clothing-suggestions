from api import getWeatherData
from weatherDataCalc import normalizedWeatherData, kelvinToFar, msToMph
from suggClothes import suggClothes

if __name__=="__main__":
    
    weatherData = getWeatherData()
    
    currTemp = weatherData['main']['temp']

    currTemp = kelvinToFar(currTemp)

    currWindSpeed = weatherData['wind']['speed']

    currWindSpeed = msToMph(currWindSpeed)

    currWeatherCond = ()
    for i in weatherData['weather']:
        currWeatherCond += (i['id'],)

    normWeatherData = normalizedWeatherData(currTemp, currWindSpeed, currWeatherCond)

    print "--------------------------------------------------------------------------"
    print "Hello! The current temperature is " + str(currTemp) + u"\u00b0" + "F."
    #print "The weather condition is "+ "."
    print ""
    print "Your suggested clothing:"
    suggClothes(normWeatherData)
    print "Have a nice day!"

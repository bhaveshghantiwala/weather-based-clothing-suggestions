'''
For any function that uses current weather condition codes
the codes refer to a id codes on the following website
https://openweathermap.org/weather-conditions
'''

from math import exp

def kelvinToFar(temp):
    temp -= 270
    temp *= 1.8
    temp += 32
    return temp

def msToMph(speed):
    speed *= 2.23694
    return speed

def tempScaleSet(temp):
    #scale: 0 - 100 based on the following function
    return 100/(1+exp(-0.07*(temp-70)))

def checkIn(tup, currWeatherCond):
    for i in tup:
        if i in currWeatherCond:
            return True
    return False

def rainScaleSet(currWeatherCond):
    #scale: 0 (no rain) to 8 (extreme/freezing rain)
    rainScale = 0
    
    if checkIn((230, 300, 310), currWeatherCond):
        rainScale = 1
    if checkIn((231, 301, 311), currWeatherCond):
        rainScale = 2
    if checkIn((232, 302, 312, 321), currWeatherCond):
        rainScale = 3
    if checkIn((200, 210, 500, 520), currWeatherCond):
        rainScale = 4
    if checkIn((201, 211, 313, 501, 521), currWeatherCond):
        rainScale = 5
    if checkIn((202, 212, 314, 502, 522), currWeatherCond):
        rainScale = 6
    if checkIn((221, 503, 531), currWeatherCond):
        rainScale = 7
    if checkIn((504, 511), currWeatherCond):
        rainScale = 8
    
    return rainScale

def snowScaleSet(currWeatherCond):
    #scale: 0 (no snow) to 3 (heavy snow)
    snowScale = 0
    
    if checkIn((600, 615, 620), currWeatherCond):
        snowScale = 1
    if checkIn((601, 611, 616, 621), currWeatherCond):
        snowScale = 2
    if checkIn((602, 612, 622), currWeatherCond):
        snowScale = 3
    
    return snowScale

def dangerCondSet(currWeatherCond):
    if checkIn((762, 781, 958, 959, 961, 962), currWeatherCond):
        return True
    else:
        return False

def windChillCalc(currTemp, currWindSpeed):
    t = currTemp
    v = currWindSpeed
    return 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)

def normalizedWeatherData(currTemp, currWindSpeed, currWeatherCond):
    '''
    This function normalizes the data from the API into data
    that can be used with the weights defined in the clothing
    classes.
    '''

    #factor in wind chill if temperature is below 50
    #and the wind speed is above 3 mph
    if (currTemp < 50 and currWindSpeed > 3):
        currTemp = windChillCalc(currTemp, currWindSpeed)

    tempScale = tempScaleSet(currTemp)
    rainScale = rainScaleSet(currWeatherCond)
    snowScale = snowScaleSet(currWeatherCond)

    #for dangerous weather
    dangerCond = dangerCondSet(currWeatherCond)
    
    dataTuple = (tempScale, rainScale, snowScale, currWindSpeed, dangerCond)
    return dataTuple

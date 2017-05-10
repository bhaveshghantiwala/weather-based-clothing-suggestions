from clothingLibrary import *
from searchIndex import searchIndex

def suggClothes(normWeatherData):
    u = upperBodyLib[searchIndex(upperBodyLib, normWeatherData[0])].getClothingName()
    l = lowerBodyLib[searchIndex(lowerBodyLib, normWeatherData[0])].getClothingName()
    f = footwearLib[searchIndex(footwearLib, normWeatherData[0])].getClothingName()
    o = outerwearLib[searchIndex(outerwearLib, normWeatherData[0])].getClothingName()

    return (u, l, f, o)

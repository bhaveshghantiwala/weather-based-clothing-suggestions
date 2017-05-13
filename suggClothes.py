from clothingLibrary import *
from searchIndex import searchIndex
from weatherDataCalc import tempScaleSet 

'''
normWeatherData contains the following tuple
(tempScale, rainScale, snowScale, currWindSpeed, dangerCond)

from clothing library these libraries are imported (sorted tuple form)
upperBodyLib
lowerBodyLib
wholeBodyLib
footwearLib
headwearLib
outerwearLib

funtions that can be used on indexes of of the lib
getClothingName()
getClothingType()
getTempRating()
getRainRating()
getSnowRating()
getWindRating() - only for outerwear
'''

def setWCheck():
    #checks if the user wants suggestions for whole body clothing
    print "Would you like suggestions for whole body clothing"
    print "rather than upper body and lower body clothing?"
    while True:
        check = raw_input("Type yes or no and press ENTER. ")
        if check == 'yes':
            return True
        elif check == 'no':
            return False
        else:
            print "Invalid input. Try again."

def setHCheck():
    #checks if the user wants suggestions for headwear
    print "Would you like suggestions for headwear?"
    while True:
        check = raw_input("Type yes or no and press ENTER. ")
        if check == 'yes':
            return True
        elif check == 'no':
            return False
        else:
            print "Invalid input. Try again."

def setOCheck(normWeatherData):
    if normWeatherData[0] < tempScaleSet(60):
        return True
    else:
        return False

def geoSeq(index, suggNum):
    if suggNum % 2:
        return index - suggNum
    else:
        return index + suggNum

def geoSeqBack(index, suggNum):
    if suggNum % 2:
        return index + suggNum
    else:
        return index - suggNum

def printClothingName(clothingType, indexDict, suggNumDict):

    if clothingType == 'u':
        library = upperBodyLib
        clothingStatement = "Upper Body: "
    elif clothingType == 'l':
        library = lowerBodyLib
        clothingStatement = "Lower Body: "
    elif clothingType == 'w':
        library = wholeBodyLib
        clothingStatement = "Whole Body: "
    elif clothingType == 'f':
        library = footwearLib
        clothingStatement = "Footwear  : "
    elif clothingType == 'h':
        library = headwearLib
        clothingStatement = "Headwear  : "
    elif clothingType == 'o':
        library = outerwearLib
        clothingStatement = "Outerwear : "

    try:
        indexErrorCnt = 0
        print clothingStatement + library[indexDict[clothingType]].getClothingName()
    except IndexError:
        indexErrorCnt = 1
        indexDict[clothingType] = geoSeqBack(indexDict[clothingType], suggNumDict[clothingType])
        suggNumDict[clothingType] -= 1
        print clothingStatement + library[indexDict[clothingType]].getClothingName()

    return indexErrorCnt

def suggClothes(normWeatherData):

    wCheck = setWCheck()
    hCheck = setHCheck()
    oCheck = setOCheck(normWeatherData)


    #keeps track of how many suggestions have been made
    #for each type of clothing
   
    suggNumDict = {'u': 0, 'l': 0, 'w': 0, 'f': 0, 'h': 0, 'o': 0}

    #find the index in the Libraries of each type of clothing
    #based on the temperature
    indexDict = {
            'u': searchIndex(upperBodyLib, normWeatherData[0]),
            'l': searchIndex(lowerBodyLib, normWeatherData[0]),
            'w': searchIndex(wholeBodyLib, normWeatherData[0]),
            'f': searchIndex(footwearLib, normWeatherData[0]),
            'h': searchIndex(headwearLib, normWeatherData[0]),
            'o': searchIndex(outerwearLib, normWeatherData[0])
            }

    while True:

        indexErrorCnt = 0

        indexDict['u'] = geoSeq(indexDict['u'], suggNumDict['u'])
        indexDict['l'] = geoSeq(indexDict['l'], suggNumDict['l'])
        indexDict['w'] = geoSeq(indexDict['w'], suggNumDict['w'])
        indexDict['f'] = geoSeq(indexDict['f'], suggNumDict['f'])
        indexDict['h'] = geoSeq(indexDict['h'], suggNumDict['h'])
        indexDict['o'] = geoSeq(indexDict['o'], suggNumDict['o'])

        if wCheck:
            indexErrorCnt += printClothingName('w', indexDict, suggNumDict)
        else:
            indexErrorCnt += printClothingName('u', indexDict, suggNumDict)
            indexErrorCnt += printClothingName('l', indexDict, suggNumDict)
       
        #for footwear
        indexErrorCnt += printClothingName('f', indexDict, suggNumDict)

        if hCheck:
            indexErrorCnt += printClothingName('h', indexDict, suggNumDict)

        if oCheck:
            indexErrorCnt += printClothingName('o', indexDict, suggNumDict)

        if indexErrorCnt > 0:
            print "There are no more options for the clothing type"
            print "you wished to change."
        
        print "If you want to change an article of clothing type"
        print "the first letter of the clothing type in lower case"
        print "and press ENTER."
        print "Otherwise, leave the field blank and press ENTER."
        changeClothing = raw_input("")

        if changeClothing == "":
            break
        elif changeClothing == "u":
            suggNumDict['u'] += 1
        elif changeClothing == "l":
            suggNumDict['l'] += 1
        elif changeClothing == "w":
            suggNumDict['w'] += 1
        elif changeClothing == "f":
            suggNumDict['f'] += 1
        elif changeClothing == "h":
            suggNumDict['h'] += 1
        elif changeClothing == "o":
            suggNumDict['o'] += 1
        else:
            print "Invalid input. Try again."


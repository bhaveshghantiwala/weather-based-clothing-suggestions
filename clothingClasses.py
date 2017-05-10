class clothing:
    '''
    clothing type codes are:
    upper body: 'u'
    lower body: 'l'
    whole body: 'w'
    outerwear : 'o'
    footwear  : 'f'
    headwear  : 'h'
    '''
    def __init__(self, clothingName, clothingType, tempRating, rainRating, snowRating):
        self.clothingName = clothingName
        self.clothingType = clothingType
        self.tempRating = tempRating
        self.rainRating = rainRating
        self.snowRating = snowRating

    def getClothingName(self):
        return self.clothingName

    def getClothingType(self):
        return self.clothingType

    def getTempRating(self):
        return self.tempRating

    def getRainRating(self):
        return self.rainRating

    def getSnowRating(self):
        return self.snowRating

class upperBody(clothing):

    def __init__(self, clothingName, tempRating, rainRating, snowRating):
        clothing.__init__(self,clothingName,'u',tempRating,rainRating,snowRating)

class lowerBody(clothing):

    def __init__(self, clothingName, tempRating, rainRating, snowRating):
        clothing.__init__(self,clothingName,'l',tempRating,rainRating,snowRating)

class wholeBody(clothing):

    def __init__(self, clothingName, tempRating, rainRating, snowRating):
        clothing.__init__(self,clothingName,'w',tempRating,rainRating,snowRating)

class footwear(clothing):

    def __init__(self, clothingName, tempRating, rainRating, snowRating):
        clothing.__init__(self,clothingName,'f',tempRating,rainRating,snowRating)

class headwear(clothing):

    def __init__(self, clothingName, tempRating, rainRating, snowRating):
        clothing.__init__(self,clothingName,'h',tempRating,rainRating,snowRating)

class outerwear(clothing):

    def __init__(self, clothingName, tempRating, rainRating, snowRating, windRating):
        clothing.__init__(self,clothingName,'o',tempRating,rainRating,snowRating)
        self.windRating = windRating

    def getWindRating(self):
        return self.windRating

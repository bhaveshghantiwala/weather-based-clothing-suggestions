from clothingClasses import *
from weatherDataCalc import tempScaleSet 

'''
Rules for addding objects to tuples
-set a tempRating value with tempScaleSet
 and a temp in farenheit
-rainRating and snowRating are the maximum tolerable
    -rain 0 - 8
    1 - light drizzle
    2 - medium drizzle
    3 - heavy drizzle
    4 - light rain
    5 - medium rain
    6 - heavy rain
    7 - very heavy rain
    8 - extreme rain
    -snow 0 - 3
    1 - light snow
    2 - medium snow
    3 - heavy snow
-windRating is the maximum tolerable mph of wind
'''

#upper body
upperBodyLib = (
        upperBody('T-Shirt', tempScaleSet(75), 0, 0),
        upperBody('Long Sleeve Shirt', tempScaleSet(65), 2, 0),
        upperBody('Thermal Shirt', tempScaleSet(50), 2, 0),
        upperBody('Tank Top', tempScaleSet(90), 0, 0)
        )

upperBodyLib = sorted(upperBodyLib, key=lambda x: x.tempRating)

#lower body
lowerBodyLib = (
        lowerBody('Jeans', tempScaleSet(60), 4, 1),
        lowerBody('Chinos', tempScaleSet(65), 3, 0),
        lowerBody('Shorts', tempScaleSet(85), 0, 0),
        lowerBody('Jeans + Thermal Pants', tempScaleSet(35), 4, 1)
        )

lowerBodyLib = sorted(lowerBodyLib, key=lambda x: x.tempRating)

#whole body
wholeBodyLib = (
        wholeBody('Sundress', tempScaleSet(80), 0, 0),
        )

#footwear
footwearLib = (
        footwear('Sandels', tempScaleSet(80), 0, 0),
        footwear('Tennis Shoes', tempScaleSet(70), 3, 0),
        footwear('Boots', tempScaleSet(60), 6, 1),
        footwear('Snow Shoes', tempScaleSet(30), 8, 3)
        )

footwearLib = sorted(footwearLib, key=lambda x: x.tempRating)

#headwear
headwearLib = (
        headwear('Baseball Cap', tempScaleSet(80), 2, 0),
        )

#outerwear
outerwearLib = (
        outerwear('Cardigan', tempScaleSet(60), 1, 0, 0),
        outerwear('Wind Breaker', tempScaleSet(55), 8, 2, 20),
        outerwear('Blazer', tempScaleSet(55), 2, 0, 10),
        outerwear('Snow Jacket', tempScaleSet(30), 8, 3, 20)
        )

outerwearLib = sorted(outerwearLib, key=lambda x: x.tempRating)

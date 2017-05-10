def binSearchTemp(tup, tempRating):
    if len(tup) == 1:
        return tup[0] #return the entire object
    else:
        midIndex = len(tup)/2
        if tempRating < tup[midIndex].getTempRating():
            return binSearchTemp(tup[:midIndex],tempRating)
        else:
            return binSearchTemp(tup[midIndex:],tempRating)

def searchIndex(tup, tempRating):
    obj = binSearchTemp(tup, tempRating)
    return tup.index(obj)

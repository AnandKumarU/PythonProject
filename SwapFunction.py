def SwapList(newList):
    size= len(newList)

    #Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1 ] = temp

    return newList

#DriverCode

    newList = [12, 35, 9, 56, 24]
    print(SwapList(newList))
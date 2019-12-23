import sys

def checkDouble(numberStr):
    containsDouble = False
    lastchar = numberStr[0]
    sameCount = 0 
    for i in range(1, len(numberStr)):
        if(numberStr[i] == lastchar):
            sameCount = sameCount + 1
            if(sameCount == 1):
                containsDouble = True
            else:
                containsDouble = False
        if(numberStr[i] != lastchar and sameCount == 1):
            containsDouble = True
            break
        elif(numberStr[i] != lastchar and sameCount > 1):
            containsDouble = False
            sameCount = 0
        lastchar = numberStr[i]
    return containsDouble

def checkNeverDecrease(numberStr):
    neverDecrease = True

    lastInt = int(numberStr[0])

    for i in range(1, len(numberStr)):
        currentInt = int(numberStr[i])
        if(currentInt < lastInt):
            neverDecrease = False
            break
        lastInt = currentInt
    return neverDecrease
        


with open(sys.argv[1]) as fp:
    puzzleinput = fp.readline()

    puzzleinput = puzzleinput.split("-")

    puzzleinput = [int(puzzleinput[0]), int(puzzleinput[1])]
    count = 0
    for number in range(puzzleinput[0], puzzleinput[1] +1):
        numberStr = str(number)

        if(not checkDouble(numberStr)):
            continue
        
        if(not checkNeverDecrease(numberStr)):
            continue
        count = count + 1
    
    print(count)
        
        

            
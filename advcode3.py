
class cord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def findCord(currentCord, input):
    value = int(input[1:len(input)])
    if(input[0] == "R"):
        return cord(currentCord.x + value, currentCord.y) 
    elif(input[0] == "L"):
        return cord(currentCord.x - value, currentCord.y)
    elif(input[0] == "U"):
        return cord(currentCord.x, currentCord.y + value)
    elif(input[0] == "D"):
        return cord(currentCord.x, currentCord.y - value)

def checkLineIntersection(X1, Y1, X2, Y2, X3, Y3, X4, Y4, intersectionCords):
    if (max(X1,X2) < min(X3,X4)):
        return
    if(max(Y1, Y2) < min(Y3, Y4)):
        return
    if(min(Y1, Y2) > max(Y3,Y4)):
        return
    if(min(X1, X2) > max(X3,X4)):
        return
    
    xDiff1 = X1-X2
    xDiff2 = X3-X4
    yDiff1 = Y1-Y2
    yDiff2 = Y3-Y4

    if(xDiff1 == 0 and xDiff2 == 0):
        return
    if(yDiff1 == 0 and yDiff2 == 0):
        return

    if(yDiff1 == 0):
        Xa = X3
        Ya = Y1
        intersectionCords.append(cord(Xa, Ya))
    elif(xDiff1 == 0):
        Xa = X1
        Ya = Y3
        intersectionCords.append(cord(Xa, Ya))
    """
    A1 = (yDiff1)/(xDiff1)  # Pay attention to not dividing by zero
    A2 = (yDiff2)/(xDiff2)  # Pay attention to not dividing by zero
    b1 = Y1-A1*X1
    b2 = Y3-A2*X3

    if (A1 == A2):
        print("paralell")
        print(A1, xDiff1, yDiff1)
        return
    Ya = A1 * Xa + b1
    Xa = (b2 - b1) / (A1 - A2)

    if ( (Xa < max( min(X1,X2), min(X3,X4) )) or
         (Xa > min( max(X1,X2), max(X3,X4) )) ):
        print("out of bound x")
        return # intersection is out of bound
    elif( (Ya < max( min(Y1,Y2), min(Y3,Y4) )) or
          (Ya > min( max(Y1, Y2), max(Y3,Y4) )) ):
        print("out of bound y")
        return # intersection is out of bound
    else:
        intersectionCords.append(cord(Xa, Ya))
    """

with open("codeinput.txt") as fp:
    line1 = fp.readline()
    line2 = fp.readline()
    line1 = line1.split(",")
    line2 = line2.split(",")
    length = len(line1)
    line1[length-1] = line1[length-1].rstrip()
    line2[length-1] = line2[length-1].rstrip()

    #print(line1)
    #print(line2)

    line1Cords = []
    line2Cords = []


    currentCord1 = cord(0,0)
    currentCord2 = cord(0,0)
    for i in range(0,length):
        line1Cords.append(findCord(currentCord1, line1[i]))
        currentCord1.x = line1Cords[i].x
        currentCord1.y = line1Cords[i].y

        line2Cords.append(findCord(currentCord2, line2[i]))
        currentCord2.x = line2Cords[i].x
        currentCord2.y = line2Cords[i].y
    
    intersectionCords = []
    for i in range(0, len(line1Cords) -1):
        for j in range(0, len(line2Cords) -1):
            checkLineIntersection(line1Cords[i].x, line1Cords[i].y, 
                                  line1Cords[i+1].x, line1Cords[i+1].y,
                                  line2Cords[j].x, line2Cords[j].y,
                                  line2Cords[j+1].x, line2Cords[j+1].y,
                                  intersectionCords)
    
    
    #for i in range(0, len(intersectionCords)):
    #    print(intersectionCords[i].x , intersectionCords[i].y)
    #print(len(intersectionCords))

    mindist = 9999999999

    for c in intersectionCords:
        distance = abs(c.x) + abs(c.y)
        if(distance < mindist):
            mindist = distance
    
    print(mindist)
        
    
    #for cord in line1Cords:
    #    print(cord.x, cord.y)
    #for cord in line2Cords:
    #    print(cord.x, cord.y)
    #print(len(line1))
    #print(len(line2))


    




    


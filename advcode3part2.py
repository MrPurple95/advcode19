
class cord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "[%d, %d]" % (self.x, self.y)
    def __repr__(self):
        return "[%d, %d]" % (self.x, self.y)

def findCord(currentCord, input1):
    value = int(input1[1:len(input1)])
    if(input1[0] == "R"):
        return cord(currentCord.x + value, currentCord.y) 
    elif(input1[0] == "L"):
        return cord(currentCord.x - value, currentCord.y)
    elif(input1[0] == "U"):
        return cord(currentCord.x, currentCord.y + value)
    elif(input1[0] == "D"):
        return cord(currentCord.x, currentCord.y - value)

def checkLineIntersection(X1, Y1, X2, Y2, X3, Y3, X4, Y4, intersectionCords):
    if(max(X1,X2) < min(X3,X4)):
        return False
    if(max(Y1, Y2) < min(Y3, Y4)):
        return False
    if(min(Y1, Y2) > max(Y3,Y4)):
        return False
    if(min(X1, X2) > max(X3,X4)):
        return False
    
    xDiff1 = X1-X2
    xDiff2 = X3-X4
    yDiff1 = Y1-Y2
    yDiff2 = Y3-Y4

    if(xDiff1 == 0 and xDiff2 == 0):
        return False
    if(yDiff1 == 0 and yDiff2 == 0):
        return False

    if(yDiff1 == 0):
        Xa = X3
        Ya = Y1
        intersectionCords.append(cord(Xa, Ya))
        return True
    elif(xDiff1 == 0):
        Xa = X1
        Ya = Y3
        intersectionCords.append(cord(Xa, Ya))
        return True
    else:
        #print("Xdiff1= %d, x1 = %d, x2 = %d" % (xDiff1, X1, X2))
        #print("Ydiff1= %d  y1 = %d , y2 = %d" % (yDiff1, Y1, Y2))
        #print("Xdiff2= %d, x3 = %d, x4 = %d" % ( xDiff2, X3, X4))
        #print("Ydiff2= %d  y3 = %d , y4 = %d" % (yDiff2, Y3, Y4))
        return False

import sys
with open(sys.argv[1]) as fp:
    line1 = fp.readline()
    line2 = fp.readline()
    line1 = line1.split(",")
    line2 = line2.split(",")
    length1 = len(line1)
    length2 = len(line2)
    line1[length1-1] = line1[length1-1].rstrip()
    line2[length2-1] = line2[length2-1].rstrip()

    line1Cords = []
    line2Cords = []


    currentCord1 = cord(0,0)
    currentCord2 = cord(0,0)
    for i in range(0,length1):
        line1Cords.append(findCord(currentCord1, line1[i]))
        currentCord1.x = line1Cords[i].x
        currentCord1.y = line1Cords[i].y
        if(i < length2):
            line2Cords.append(findCord(currentCord2, line2[i]))
            currentCord2.x = line2Cords[i].x
            currentCord2.y = line2Cords[i].y
    
    intersectionCords = []
    intersectionIndex = []
    sum1List = []
    sum2List = []
    sumOfSteps1 = 0
    for i in range(0, len(line1Cords)):
        input1 = line1[i]
        value1 = int(input1[1:len(input1)])
        sumOfSteps2 = 0
        for j in range(0, len(line2Cords)):
            isIntersection = False
            input2 = line2[j]
            value2 = int(input2[1:len(input2)])
            if(i > 0 and j > 0):
                isIntersection = checkLineIntersection(line1Cords[i-1].x, line1Cords[i-1].y, 
                                        line1Cords[i].x, line1Cords[i].y,
                                        line2Cords[j-1].x, line2Cords[j-1].y,
                                        line2Cords[j].x, line2Cords[j].y,
                                        intersectionCords)
            elif(i == 0 and j > 0):
                isIntersection = checkLineIntersection(0, 0, 
                                        line1Cords[i].x, line1Cords[i].y,
                                        line2Cords[j-1].x, line2Cords[j-1].y,
                                        line2Cords[j].x, line2Cords[j].y,
                                        intersectionCords)
            elif(j == 0 and i > 0):
                isIntersection = checkLineIntersection(line1Cords[i-1].x, line1Cords[i-1].x, 
                                        line1Cords[i].x, line1Cords[i].y,
                                        0, 0,
                                        line2Cords[j].x, line2Cords[j].y,
                                        intersectionCords)
            if(i == 0 and j == 0):
                isIntersection = checkLineIntersection(0, 0, 
                                        line1Cords[i].x, line1Cords[i].y,
                                        0, 0,
                                        line2Cords[j].x, line2Cords[j].y,
                                        intersectionCords)
            if(isIntersection):
                intersectionIndex.append([i,j])
                c1 = cord(0,0)
                if(i > 0):
                    c1 = line1Cords[i-1]
                c2 = line1Cords[i]
                c3 = cord(0,0)
                if(j > 0):
                    c3 = line2Cords[j-1]
                c4 = line2Cords[j]


                if(c1.x == c2.x):

                    sum1List.append(sumOfSteps1 + abs(c1.y-c3.y))
                    sum2List.append(sumOfSteps2 + abs(c1.x-c3.x))
                else:
                    sum1List.append(sumOfSteps1 + abs(c1.x-c3.x))
                    sum2List.append(sumOfSteps2 + abs(c1.y-c3.y))
            sumOfSteps2 += value2

        sumOfSteps1 += value1

    mindist = 9999999999


    for c in intersectionCords:
        distance = abs(c.x) + abs(c.y)
        if(distance < mindist):
            mindist = distance
    
    sumlist = []
    for i in range(0, len(sum1List)):
        sumlist.append(sum1List[i] + sum2List[i])

    sumlist.sort()
    print(mindist)
    print(sumlist[0])
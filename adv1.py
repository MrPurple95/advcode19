import math
with open('advcode1.txt') as fp:
    mass = fp.readline()
    
    totalFuel = 0
    while mass:
        fuelReq = math.floor(int(mass)/3) - 2
        totalFuel += fuelReq
        fuelReq = math.floor(int(fuelReq)/3) - 2
        while fuelReq > 0:
            totalFuel += fuelReq
            fuelReq = math.floor(int(fuelReq)/3) - 2

        mass = fp.readline()
    print(totalFuel)

carPos = [0,0]
locs = dict()
def main():
    goingBack = False
    size = int(input())
    O = int(input())
    for i in range(O):
        x,y,price = map(int, input().split())
        if(x not in locs):
            locs[x] = dict()
        if(y not in locs[x]):
            locs[x][y] = price
    orderValue = 0
    while True:
        biggestRange = 0
        if(size - carPos[1] > biggestRange):
            biggestRange = size - carPos[1]
        if(carPos[1] - size > biggestRange):
            biggestRange = carPos[1] - size 
        if(carPos[0] - size > biggestRange):
            biggestRange = carPos[0] - size
        if(size - carPos[0] > biggestRange):
            biggestRange = size - carPos[0]
        # print(carPos)
        missingoutY = tallyVertical(goingBack,size,biggestRange)
        missingoutX = tallyHorizontal(goingBack,size,biggestRange)
        dir = 1
        if(goingBack):

            dir = -1
        if(missingoutX == -1 and missingoutY == -1):
            # print("at end")
            if(goingBack):
                print(orderValue)
                return
            else:
                goingBack = True
                continue
        if(missingoutX > missingoutY):
            carPos[0]+=dir
        else:
            carPos[1]+=dir
        if GetAtBoardLoc(carPos[0],carPos[1]) >0:
            orderValue += locs[x][y]
            locs[x][y] = 0
        
        
        
def tallyVertical(goingBack,size,biggestRange):
    total = 0
    if(not goingBack):
        if(carPos[1] == size-1):
            return -1
        counter = 0
        for i in range(carPos[1],size):
            counter += 1
            total += GetAtBoardLoc(carPos[0],i)

        avg = total/size
        extra = biggestRange - counter
        total += avg*extra
    else:
        if(carPos[1] == 0):
            return -1
        counter = 0
        for i in range(size,carPos[1],-1):
            counter += 1
            total += GetAtBoardLoc(carPos[0],i)
        avg = total/size
        extra = biggestRange - counter
        total += avg*extra
    return total

def tallyHorizontal(goingBack,size,biggestRange):
    total = 0

    if(not goingBack):
        if(carPos[0] == size-1):
            return -1
        counter = 0 
        for i in range(carPos[0],size):
            counter += 1
            total += GetAtBoardLoc(i,carPos[1])
        avg = total/size
        extra = biggestRange - counter
        total += avg*extra
    else:
        if(carPos[0] == 0):
            return -1
        counter = 0
        for i in range(size,carPos[0],-1):
            counter += 1
            total += GetAtBoardLoc(i,carPos[1])
        avg = total/size
        extra = biggestRange - counter
        total += avg*extra
    return total

def GetAtBoardLoc(x,y):
    if(x not in locs):  
        return 0
    if(y not in locs[x]):
        return 0
    return locs[x][y]

main()